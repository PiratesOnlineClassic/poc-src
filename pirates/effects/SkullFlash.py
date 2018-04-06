# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.SkullFlash
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import *
from EffectController import EffectController
from pandac.PandaModules import *
from PooledEffect import PooledEffect


class SkullFlash(PooledEffect, EffectController):
    __module__ = __name__

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.fadeTime = 0.15
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModelCopy('models/effects/particleCards')
        self.effectModel = model.find('**/particleSkullGlow')
        self.effectModel2 = self.attachNewNode('effectModelCopy')
        self.effectModel.instanceTo(self.effectModel2)
        self.effectModel.setBillboardPointWorld()
        self.effectModel.reparentTo(self)
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.effectModel.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setDepthWrite(0)
        self.setFogOff()

    def createTrack(self):
        self.effectModel.setColorScale(0, 0, 0, 0)
        fadeBlast = self.effectModel.colorScaleInterval(self.fadeTime, Vec4(0, 0, 0, 0), startColorScale=Vec4(self.effectColor), blendType='easeOut')
        scaleBlast = self.effectModel.scaleInterval(self.fadeTime, 2.0, startScale=1.0, blendType='easeOut')
        self.track = Sequence(Parallel(fadeBlast, scaleBlast), Func(self.cleanUpEffect))

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompiling .\pirates\effects\SkullFlash.pyc
