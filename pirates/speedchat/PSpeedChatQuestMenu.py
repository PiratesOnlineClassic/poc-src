# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.speedchat.PSpeedChatQuestMenu
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.speedchat.SCTerminal import *
from pirates.pirate.LocalPirate import *
from pirates.quest.Quest import Quest
from pirates.quest.QuestDNA import *
from pirates.quest.QuestStatus import *
from pirates.speedchat.PSpeedChatQuestTerminal import *


class PSpeedChatQuestMenu(SCMenu):
    __module__ = __name__

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('localAvatarQuestAdded', self.__questMenuRefresh)
        self.accept('localAvatarQuestUpdate', self.__questMenuRefresh)
        self.accept('localAvatarQuestItemUpdate', self.__questMenuRefresh)
        self.accept('localAvatarQuestComplete', self.__questMenuRefresh)
        self.accept('localAvatarQuestDeleted', self.__questMenuRefresh)

    def destroy(self):
        SCMenu.destroy(self)

    def __questMenuRefresh(self, quest, item=None, note=None):
        self.clearMenu()
        quests = localAvatar.questStatus.getCurrentQuests()
        if quests is None:
            return
        for quest in quests:
            q = quest
            if q is None:
                continue
            self.__questAddSCChat(q)

        return

    def __questAddSCChat(self, quest):
        qId = quest.questId
        qDNA = QuestDB.QuestDict[qId]
        qInt = qDNA.questInt
        i = 0
        for task in quest.questDNA.getTasks():
            if len(quest.getSCSummaryText(0)) > 2:
                self.append(PSpeedChatQuestTerminal(quest.getSCSummaryText(i), qInt, quest.giverId, 0, i))
            if len(quest.getSCWhereIsText(0)) > 2:
                self.append(PSpeedChatQuestTerminal(quest.getSCWhereIsText(i), qInt, quest.giverId, 1, i))
            if len(quest.getSCHowToText(0)) > 2:
                self.append(PSpeedChatQuestTerminal(quest.getSCHowToText(i), qInt, quest.giverId, 2, i))
            i = i + 1
# okay decompiling .\pirates\speedchat\PSpeedChatQuestMenu.pyc
