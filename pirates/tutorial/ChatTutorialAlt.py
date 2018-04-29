import random
import time

from direct.showbase import DirectObject
from panda3d.core import *
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import NewTutorialPanel
from pirates.tutorial import TutorialGlobals


class ChatTutorialAlt(DirectObject.DirectObject):
    notify = directNotify.newCategory('ChatTutorialAlt')

    def __init__(self):
        self.stage = 0
        self.panel1 = None
        self.panel2 = None
        self.panel3 = None
        self.panel4 = None
        self.panel5 = None
        self.contentPart1 = 'chat_tut_alt1'
        self.contentPart2 = 'chat_tut_alt2'
        self.contentPart3 = 'chat_tut_alt3'
        self.contentPart4 = 'chat_tut_alt4'
        self.contentPart5 = 'chat_tut_alt5'
        self.showPart1()
        return

    def __handleOKButton(self):
        messenger.send('closeTutorialWindow')
        self.showPart2()

    def __handleOpenSpeedChatWindow(self):
        messenger.send('closeTutorialWindow')
        self.showPart3()

    def __handleSentSpeedChat(self):
        messenger.send('closeTutorialWindow')
        self.showPart4()

    def __handleOKButton2(self):
        messenger.send('closeTutorialWindow')
        self.showPart5()

    def __handleOKButton3(self):
        self.panelCleanup()
        self.ignoreAll()
        self.destroy()

    def showPart1(self):
        self.panel1 = NewTutorialPanel.NewTutorialPanel([self.contentPart1, 'test1'])
        self.panel1.activate()
        self.updateTutorialState()
        self.panel1.setYesCommand(self.__handleOKButton)
        self.stage = 1

    def showPart2(self):
        if self.stage != 1:
            return
        self.panel2 = NewTutorialPanel.NewTutorialPanel([self.contentPart2])
        self.panel2.activate()
        self.acceptOnce('openedSpeedChat', self.__handleOpenSpeedChatWindow)
        self.stage = 2

    def showPart3(self):
        if self.stage != 2:
            return
        self.panel3 = NewTutorialPanel.NewTutorialPanel([self.contentPart3])
        self.panel3.activate()
        self.acceptOnce('sentSpeedChat', self.__handleSentSpeedChat)
        self.stage = 3

    def showPart4(self):
        if self.stage != 3:
            return
        self.panel4 = NewTutorialPanel.NewTutorialPanel([self.contentPart4, 'test2'])
        self.panel4.activate()
        self.panel4.setYesCommand(self.__handleOKButton2)
        self.stage = 4

    def showPart5(self):
        if self.stage != 4:
            return
        self.panel5 = NewTutorialPanel.NewTutorialPanel([self.contentPart5, 'test3'])
        self.panel5.activate()
        self.panel5.setYesCommand(self.__handleOKButton3)
        self.stage = 5

    def updateTutorialState(self):
        base.localAvatar.b_setTutorial(PiratesGlobals.TUT_INTRODUCTION_TO_FRIENDS)

    def panelCleanup(self):
        messenger.send('closeTutorialWindowAll')

    def destroy(self):
        del self.stage
        del self.panel1
        del self.panel2
        del self.panel3
        del self.panel4
        del self.panel5
        del self.contentPart1
        del self.contentPart2
        del self.contentPart3
        del self.contentPart4
        del self.contentPart5

    def doNothing(self):
        pass