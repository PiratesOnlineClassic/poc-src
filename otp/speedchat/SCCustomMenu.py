from otp.otpbase.OTPLocalizer import CustomSCStrings
from otp.speedchat.SCCustomTerminal import SCCustomTerminal
from otp.speedchat.SCMenu import SCMenu


class SCCustomMenu(SCMenu):

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('customMessagesChanged', self.__customMessagesChanged)
        self.__customMessagesChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def __customMessagesChanged(self):
        self.clearMenu()

        try:
            lt = base.localAvatar
        except BaseException:
            return

        if lt:
            for msgIndex in lt.customMessages:
                if msgIndex in CustomSCStrings:
                    self.append(SCCustomTerminal(msgIndex))
