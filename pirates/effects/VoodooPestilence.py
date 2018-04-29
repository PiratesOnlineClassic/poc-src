# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.VoodooPestilence
import random

from direct.actor import Actor
from direct.interval.IntervalGlobal import *
from direct.particles import ForceGroup, ParticleEffect, Particles
from pirates.effects.EffectController import EffectController
from panda3d.core import *
from pirates.effects.PooledEffect import PooledEffect


class VoodooPestilence(PooledEffect, EffectController):
    
    cardScale = 64.0

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModelCopy('models/effects/particleMaps')
        self.card = model.find('**/particleEvilSmoke')
        self.effectScale = 1.0
        if not self.particleDummy:
            self.particleDummy = render.attachNewNode(ModelNode('selfParticleDummy'))
            self.particleDummy.setDepthWrite(0)
            self.particleDummy.setColorScaleOff()
            self.particleDummy.setLightOff()
            self.particleDummy.setFogOff()
        self.f = ParticleEffect.ParticleEffect()
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereVolumeEmitter')
        self.f.addParticles(self.p0)
        self.f.setP(90.0)
        self.p0.setPoolSize(256)
        self.p0.setBirthRate(0.01)
        self.p0.setLitterSize(3)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(0)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(1.2)
        self.p0.factory.setLifespanSpread(0.2)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(360.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(300.0)
        self.p0.factory.setAngularVelocitySpread(25.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OOneMinusFbufferAlpha, ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1.0, 1.0, 1.0, 1.0), Vec4(0.1, 0.2, 0.1, 0.5), 1)

    def createTrack(self):
        self.p0.renderer.setInitialXScale(0.003 * self.effectScale * self.cardScale)
        self.p0.renderer.setFinalXScale(0.0001 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.0015 * self.effectScale * self.cardScale)
        self.p0.renderer.setFinalYScale(0.0001 * self.cardScale)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(0.3)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, -0.45))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.01)
        if self.effectScale > 1.0:
            self.p0.emitter.setAmplitude(0.15)
            self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, -0.1))
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.01), Func(self.p0.clearToInitial), Func(self.f.start, self, self.particleDummy))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(2.5), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(1.25), self.endEffect)

    def cleanUpEffect(self):
        self.f.disable()
        self.detachNode()
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompiling .\pirates\effects\VoodooPestilence.pyc
