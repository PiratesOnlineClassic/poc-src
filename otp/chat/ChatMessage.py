# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.chat.ChatMessage


class ChatMessage:
    __module__ = __name__

    def __init__(self, timeStamp, type, body, flags, id, name, isPlayer, whisper, sentRatherThanReceived):
        self.timeStamp = timeStamp
        self.type = type
        self.body = body
        self.flags = flags
        self.id = id
        self.name = name
        self.isPlayer = isPlayer
        self.whisper = whisper
        self.sentRatherThanReceived = sentRatherThanReceived

    def getTimeStamp(self):
        return self.timeStamp

    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp

    def getType(self):
        return self.type

    def setType(self, type):
        self.name = type

    def getBody(self):
        return self.body

    def setBody(self, body):
        self.body = body

    def getFlags(self):
        return self.flags

    def setFlags(self, flags):
        self.flags = flags

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getIsPlayer(self):
        return self.isPlayer

    def setIsPlayer(self, isPlayer):
        self.isPlayer = isPlayer

    def getSentRatherThanReceived(self):
        return self.sentRatherThanReceived

    def setSentRatherThanReceived(self, sentRatherThanReceived):
        self.sentRatherThanReceived = sentRatherThanReceived

    def getWhisper(self):
        return self.whisper

    def setWhisper(self, whisper):
        self.whisper = whisper
# okay decompiling .\otp\chat\ChatMessage.pyc
