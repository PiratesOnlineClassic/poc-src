import random

from direct.actor import Actor
from direct.interval.IntervalGlobal import *
from direct.particles import ForceGroup, ParticleEffect, Particles
from EffectController import EffectController
from pandac.PandaModules import *
from PooledEffect import PooledEffect


class WindCharge(PooledEffect, EffectController):

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.effectModel = loader.loadModelCopy('models/effects/windSwirl')
        self.effectModel.setTwoSided(1)
        self.inner = self.effectModel.find('**/inner')
        self.outer = self.effectModel.find('**/outer')
        self.effectModel.setColorScaleOff()
        self.effectModel.setColorScale(1, 1, 1, 0.75)
        self.effectModel.reparentTo(self)
        self.setDepthWrite(0)
        self.setColorScaleOff()
        self.setLightOff()

    def createTrack(self):
        textureStage = self.effectModel.findAllTextureStages()[0]
        self.effectModel.setTexOffset(textureStage, 0.0, 1.0)
        self.effectModel.setScale(0.5, 0.5, 0.5)
        self.duration = 2.0
        self.setColorScale(0.0, 0.0, 0.0, 0.0)
        fadeIn = LerpColorScaleInterval(self, 3.0, Vec4(1.0, 1.0, 1.0, 0.75), startColorScale=Vec4(0.0, 0.0, 0.0, 0.0))
        fadeOut = LerpColorScaleInterval(self, 1.0, Vec4(0.0, 0.0, 0.0, 0.0), startColorScale=Vec4(1.0, 1.0, 1.0, 0.75))
        rotate = LerpHprInterval(self.effectModel, 0.5, Vec3(-360, 0, 0), startHpr=Vec3(0, 0, 0))
        self.startEffect = Sequence(Func(rotate.loop), fadeIn)
        self.endEffect = Sequence(fadeOut, Func(rotate.finish), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(self.duration), self.endEffect)

    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        self.stop()
        if self.track:
            self.track = None
        self.removeNode()
        EffectController.destroy(self)
        PooledEffect.destroy(self)
        return
