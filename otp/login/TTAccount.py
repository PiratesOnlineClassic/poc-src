import copy

from otp.login import HTTPUtil
from otp.login import RemoteValueSet
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PythonUtil
from otp.otpbase import OTPLocalizer
from panda3d.core import *

accountServer = ''
accountServer = launcher.getAccountServer()
configAccountServer = base.config.GetString('account-server', '')
if configAccountServer:
    accountServer = configAccountServer
if not accountServer:
    accountServer = 'https://account.toontown.com'
accountServer = URLSpec(accountServer, 1)


def getAccountServer():
    return accountServer


TTAccountException = HTTPUtil.HTTPUtilException


class TTAccount:

    notify = DirectNotifyGlobal.directNotify.newCategory('TTAccount')

    def __init__(self, cr):
        self.cr = cr
        self.response = None
        return

    def createAccount(self, loginName, password, data):
        return self.talk('create', data=self.__makeLoginDict(
            loginName, password, data))

    def authorize(self, loginName, password):
        return self.talk(
            'play', data=self.__makeLoginDict(loginName, password))

    def createBilling(self, loginName, password, data):
        return self.talk('purchase', data=self.__makeLoginDict(
            loginName, password, data))

    def setParentPassword(self, loginName, password, parentPassword):
        return self.talk('setParentPassword', data=self.__makeLoginDict(
            loginName, password, {'parentPassword': parentPassword}))

    def supportsParentPassword(self):
        return 1

    def authenticateParentPassword(self, loginName, password, parentPassword):
        try:
            errorMsg = self.talk(
                'authenticateParentPassword',
                data=self.__makeLoginDict(
                    loginName,
                    parentPassword))
            if not errorMsg:
                return (1, None)
            if self.response.getInt('errorCode') in (5, 72):
                return (0, None)
            return (
                0, errorMsg)
        except TTAccountException as e:
            return (
                0, str(e))

        return

    def supportsAuthenticateDelete(self):
        return 1

    def authenticateDelete(self, loginName, password):
        try:
            errorMsg = self.talk(
                'authenticateDelete',
                data=self.__makeLoginDict(
                    loginName,
                    password))
            if not errorMsg:
                return (1, None)
            if self.response.getInt('errorCode') in (5, 72):
                return (0, None)
            return (
                0, errorMsg)
        except TTAccountException as e:
            return (
                0, str(e))

        return

    def enableSecretFriends(self, loginName, password,
                            parentPassword, enable=1):
        try:
            errorMsg = self.talk(
                'setSecretChat',
                data=self.__makeLoginDict(
                    loginName,
                    parentPassword,
                    {
                        'chat': base.cr.secretChatAllowed,
                        'secretsNeedParentPassword': base.cr.secretChatNeedsParentPassword}))
            if not errorMsg:
                return (1, None)
            if self.response.getInt('errorCode') in (5, 72):
                return (0, None)
            return (
                0, errorMsg)
        except TTAccountException as e:
            return (
                0, str(e))

        return

    def changePassword(self, loginName, password, newPassword):
        return self.talk('purchase', data=self.__makeLoginDict(
            loginName, password, {'newPassword': newPassword}))

    def requestPwdReminder(self, email=None, acctName=None):
        data = {}
        if email is not None:
            data['email'] = email
        else:
            data['accountName'] = acctName
        return self.talk('forgotPassword', data)

    def cancelAccount(self, loginName, password):
        return self.talk(
            'cancel', data=self.__makeLoginDict(loginName, password))

    def getAccountData(self, loginName, password):
        errorMsg = self.talk(
            'get', data=self.__makeLoginDict(
                loginName, password))
        if errorMsg:
            self.notify.warning('getAccountData error: %s' % errorMsg)
            return errorMsg
        if self.response.hasKey('errorMsg'):
            self.notify.warning(
                "error field is: '%s'" %
                self.response.getString('errorMsg'))
        self.accountData = copy.deepcopy(self.response)
        fieldNameMap = {
            'em': 'email',
            'l1': 'addr1',
            'l2': 'addr2',
            'l3': 'addr3'}
        dict = self.accountData.dict
        for fieldName in dict.keys():
            if fieldName in fieldNameMap:
                dict[fieldNameMap[fieldName]] = dict[fieldName]
                del dict[fieldName]

        return

    def getLastErrorMsg(self, forceCustServNum=0):
        errCode = self.response.getInt('errorCode')
        if errCode < 100:
            msg = self.response.getString('errorMsg')
            if forceCustServNum:
                msg += ' ' + OTPLocalizer.TTAccountCustomerServiceHelp % self.cr.accountServerConstants.getString(
                    'customerServicePhoneNumber')
        else:
            if errCode < 200:
                msg = self.response.getString('errorMsg')
                msg += ' ' + OTPLocalizer.TTAccountCustomerServiceHelp % self.cr.accountServerConstants.getString(
                    'customerServicePhoneNumber')
            else:
                if errCode >= 500:
                    msg = OTPLocalizer.TTAccountIntractibleError
                    msg += ' ' + OTPLocalizer.TTAccountCallCustomerService % self.cr.accountServerConstants.getString(
                        'customerServicePhoneNumber')
                else:
                    self.notify.warning(
                        'unknown error code class: %s: %s' %
                        (self.response.getInt('errorCode'),
                         self.response.getString('errorMsg')))
                    msg = self.response.getString('errorMsg')
                    msg += ' ' + OTPLocalizer.TTAccountCallCustomerService % self.cr.accountServerConstants.getString(
                        'customerServicePhoneNumber')
        return msg

    def __makeLoginDict(self, loginName, password, data=None):
        dict = {'accountName': loginName, 'password': password}
        if data:
            dict.update(data)
        return dict

    def talk(self, operation, data={}):
        self.notify.debug('TTAccount.talk()')
        for key in data.keys():
            data[key] = str(data[key])

        if operation in ('play', 'get', 'cancel',
                         'authenticateParentPassword', 'authenticateDelete'):
            pass
        else:
            if operation == 'forgotPassword':
                pass
            else:
                if operation == 'setParentPassword':
                    pass
                else:
                    if operation == 'setSecretChat':
                        pass
                    else:
                        if operation == 'create':
                            pass
                        else:
                            if operation == 'purchase':
                                if 'newPassword' in data:
                                    pass
                            else:
                                self.notify.error(
                                    "Internal TTAccount error: need to add 'required data' checking for %s operation" %
                                    operation)
        op2Php = {
            'play': 'play',
            'get': 'get',
            'cancel': 'cancel',
            'create': 'create',
            'purchase': 'purchase',
            'setParentPassword': 'setSecrets',
            'authenticateParentPassword': 'authenticateChat',
            'authenticateDelete': 'authDelete',
            'setSecretChat': 'setChat',
            'forgotPassword': 'forgotPw'}
        url = URLSpec(getAccountServer())
        url.setPath('/%s.php' % op2Php[operation])
        body = ''
        if 'accountName' in data:
            url.setQuery('n=%s' % URLSpec.quote(data['accountName']))
        serverFields = {
            'accountName': 'n',
            'password': 'p',
            'parentPassword': 'sp',
            'newPassword': 'np',
            'chat': 'chat',
            'email': 'em',
            'dobYear': 'doby',
            'dobMonth': 'dobm',
            'dobDay': 'dobd',
            'ccNumber': 'ccn',
            'ccMonth': 'ccm',
            'ccYear': 'ccy',
            'nameOnCard': 'noc',
            'addr1': 'l1',
            'addr2': 'l2',
            'addr3': 'l3',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'zip': 'zip',
            'referrer': 'ref',
            'secretsNeedParentPassword': 'secretsNeedsParentPassword'}
        ignoredFields = ('ccType', )
        outBoundFields = {}
        for fieldName in data.keys():
            if fieldName not in serverFields:
                if fieldName not in ignoredFields:
                    self.notify.error('unknown data field: %s' % fieldName)
            else:
                outBoundFields[serverFields[fieldName]] = data[fieldName]

        orderedFields = sorted(outBoundFields.keys())
        for fieldName in orderedFields:
            if len(body):
                body += '&'
            body += '%s=%s' % (fieldName,
                               URLSpec.quotePlus(outBoundFields[fieldName]))

        self.notify.debug('url=' + url.cStr())
        self.notify.debug('body=' + body)
        if operation in ('get', ):
            expectedHeader = 'ACCOUNT INFO'
        else:
            if operation in ('play', 'cancel', 'create', 'purchase', 'setParentPassword',
                             'setSecretChat', 'authenticateParentPassword', 'authenticateDelete',
                             'forgotPassword'):
                expectedHeader = 'ACCOUNT SERVER RESPONSE'
            else:
                self.notify.error(
                    "Internal TTAccount error: need to set expected response header for '%s' operation" %
                    operation)
        self.response = RemoteValueSet.RemoteValueSet(
            url, self.cr.http, body=body, expectedHeader=expectedHeader)
        self.notify.debug('    self.response=' + str(self.response))
        if self.response.hasKey('errorCode'):
            errorCode = self.response.getInt('errorCode')
            self.notify.info('account server error code: %s' % errorCode)
            if errorCode == 10:
                self.cr.freeTimeExpiresAt = 0
        if self.response.hasKey('errorMsg'):
            return self.getLastErrorMsg()
        if operation in ('get', 'forgotPassword', 'authenticateDelete', 'play', 'cancel',
                         'create', 'purchase', 'setParentPassword', 'authenticateParentPassword'):
            pass
        else:
            if operation == 'setSecretChat':
                self.playToken = self.response.getString('playToken')
                self.playTokenIsEncrypted = 1
            else:
                self.notify.error(
                    'Internal TTAccount error: need to extract useful data for %s operation' %
                    operation)
        return
