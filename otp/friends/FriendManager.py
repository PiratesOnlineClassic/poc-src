# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.friends.FriendManager
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from otp.otpbase import OTPGlobals
from pandac.PandaModules import *


class FriendManager(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.__available = 0
        self.gameSpecificFunction = None
        return

    def setAvailable(self, available):
        self.__available = available
        if self.__available and self.gameSpecificFunction:
            self.gameSpecificFunction()

    def getAvailable(self):
        return self.__available

    def setGameSpecificFunction(self, function):
        self.gameSpecificFunction = function

    def executeGameSpecificFunction(self):
        if self.__available and self.gameSpecificFunction:
            self.gameSpecificFunction()

    def generate(self):
        if base.cr.friendManager != None:
            base.cr.friendManager.delete()
        base.cr.friendManager = self
        DistributedObject.DistributedObject.generate(self)
        return

    def disable(self):
        base.cr.friendManager = None
        DistributedObject.DistributedObject.disable(self)
        return

    def delete(self):
        self.gameSpecificFunction = None
        base.cr.friendManager = None
        DistributedObject.DistributedObject.delete(self)
        return

    def up_friendQuery(self, inviteeId):
        self.sendUpdate('friendQuery', [inviteeId])
        self.notify.debug('Client: friendQuery(%d)' % inviteeId)

    def up_cancelFriendQuery(self, context):
        self.sendUpdate('cancelFriendQuery', [context])
        self.notify.debug('Client: cancelFriendQuery(%d)' % context)

    def up_inviteeFriendConsidering(self, yesNo, context):
        self.sendUpdate('inviteeFriendConsidering', [yesNo, context])
        self.notify.debug('Client: inviteeFriendConsidering(%d, %d)' % (yesNo, context))

    def up_inviteeFriendResponse(self, yesNoMaybe, context):
        self.sendUpdate('inviteeFriendResponse', [yesNoMaybe, context])
        self.notify.debug('Client: inviteeFriendResponse(%d, %d)' % (yesNoMaybe, context))

    def up_inviteeAcknowledgeCancel(self, context):
        self.sendUpdate('inviteeAcknowledgeCancel', [context])
        self.notify.debug('Client: inviteeAcknowledgeCancel(%d)' % context)

    def friendConsidering(self, yesNoAlready, context):
        self.notify.info('Roger Client: friendConsidering(%d, %d)' % (yesNoAlready, context))
        messenger.send('friendConsidering', [yesNoAlready, context])

    def friendResponse(self, yesNoMaybe, context):
        self.notify.debug('Client: friendResponse(%d, %d)' % (yesNoMaybe, context))
        messenger.send('friendResponse', [yesNoMaybe, context])

    def inviteeFriendQuery(self, inviterId, inviterName, inviterDna, context):
        self.notify.debug('Client: inviteeFriendQuery(%d, %s, dna, %d)' % (inviterId, inviterName, context))
        if not hasattr(base, 'localAvatar'):
            self.up_inviteeFriendConsidering(0, context)
            return
        if inviterId in base.localAvatar.ignoreList:
            self.up_inviteeFriendConsidering(4, context)
            return
        if not base.localAvatar.acceptingNewFriends:
            self.up_inviteeFriendConsidering(6, context)
            return
        self.up_inviteeFriendConsidering(self.__available, context)
        if self.__available:
            messenger.send('friendInvitation', [inviterId, inviterName, inviterDna, context])

    def inviteeCancelFriendQuery(self, context):
        self.notify.debug('Client: inviteeCancelFriendQuery(%d)' % context)
        messenger.send('cancelFriendInvitation', [context])
        self.up_inviteeAcknowledgeCancel(context)

    def up_requestSecret(self):
        self.notify.warning('Sending Request')
        self.sendUpdate('requestSecret', [])

    def requestSecretResponse(self, result, secret):
        messenger.send('requestSecretResponse', [result, secret])

    def up_submitSecret(self, secret):
        self.sendUpdate('submitSecret', [secret])

    def submitSecretResponse(self, result, avId):
        messenger.send('submitSecretResponse', [result, avId])
# okay decompiling .\otp\friends\FriendManager.pyc
