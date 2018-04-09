# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.pvp.PVPInvitee
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from otp.otpbase import OTPGlobals, OTPLocalizer
from pandac.PandaModules import *
from pirates.piratesbase import PiratesGlobals, PLocalizer
from pirates.piratesgui import GuiPanel, PDialog, PiratesGuiGlobals
from pirates.piratesgui.RequestButton import RequestButton


class PVPInviteeButton(RequestButton):
    

    def __init__(self, text, command):
        RequestButton.__init__(self, text, command)
        self.initialiseoptions(PVPInviteeButton)


class PVPInvitee(GuiPanel.GuiPanel):
    
    notify = DirectNotifyGlobal.directNotify.newCategory('PVPInvitee')

    def __init__(self, avId, avName):
        GuiPanel.GuiPanel.__init__(self, 'Skirmish Invitation', 0.5, 0.5)
        self.initialiseoptions(PVPInvitee)
        self.setPos(0.15, 0, 0.25)
        self.avId = avId
        self.avName = avName
        text = PLocalizer.PVPInviteeInvitation % self.avName
        self.message = DirectLabel(parent=self, relief=None, text=text, text_scale=PiratesGuiGlobals.TextScaleLarge, text_align=TextNode.ACenter, text_fg=PiratesGuiGlobals.TextFG2, text_shadow=PiratesGuiGlobals.TextShadow, text_wordwrap=11, pos=(0.25,
                                                                                                                                                                                                                                                      0,
                                                                                                                                                                                                                                                      0.35), textMayChange=1)
        self.bOk = PVPInviteeButton(text=OTPLocalizer.DialogOK, command=self.__handleOk)
        self.bOk.reparentTo(self)
        self.bOk.setPos(0.1, 0, 0.1)
        self.bNo = PVPInviteeButton(text=OTPLocalizer.DialogNo, command=self.__handleNo)
        self.bNo.reparentTo(self)
        self.bNo.setPos(0.3, 0, 0.1)
        self.accept('cancelChallengeInvitation', self.__handleCancelFromAbove)
        return

    def destroy(self):
        if hasattr(self, 'destroyed'):
            return
        self.destroyed = 1
        self.ignore('cancelChallengeInvitation')
        GuiPanel.GuiPanel.destroy(self)

    def __handleOk(self):
        base.cr.pvpManager.sendAcceptChallenge(self.avId)
        self.destroy()

    def __handleNo(self):
        self.destroy()

    def __handleCancelFromAbove(self):
        self.destroy()
# okay decompiling .\pirates\pvp\PVPInvitee.pyc
