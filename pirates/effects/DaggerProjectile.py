# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.effects.DaggerProjectile
import random

from direct.actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import *
from EffectController import EffectController
from pandac.PandaModules import *
from pirates.effects import PolyTrail
from pirates.piratesbase import PiratesGlobals
from PooledEffect import PooledEffect


class DaggerProjectile(PooledEffect, EffectController):
    

    def __init__(self, type=None):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.rotDummy = self.attachNewNode('rotDummy')
        self.knifeModel = loader.loadModelCopy('models/handheld/dagger_high')
        self.knifeModel.reparentTo(self.rotDummy)
        self.knifeModel.setY(-0.6)
        self.knifeModel.setR(180)
        self.motion_color = [
         Vec4(0.5, 0.6, 0.8, 1.0), Vec4(0.5, 0.6, 0.8, 1.0)]
        vertex_list = [
         Vec4(0.0, 1.0, 0.0, 1.0), Vec4(0.0, -1.0, 0.0, 1.0)]
        self.motion_trail = PolyTrail.PolyTrail(None, vertex_list, self.motion_color)
        self.motion_trail.reparentTo(self)
        vertex_list = [
         Vec4(0.3, 0.0, 0.0, 1.0), Vec4(-0.3, 0.0, 0.0, 1.0)]
        self.motion_trail2 = PolyTrail.PolyTrail(None, vertex_list, self.motion_color)
        self.motion_trail2.reparentTo(self)
        self.motion_trail.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.motion_trail2.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        return

    def createTrack(self, time, targetPos, motion_color, rate=1):
        throwTrack = LerpPosInterval(self, time, targetPos)
        if not motion_color:
            motion_color = self.motion_color
        self.motion_trail.setVertexColors(motion_color)
        self.motion_trail2.setVertexColors(motion_color)
        offset = random.uniform(0.0, 360.0)
        hOffset = random.uniform(-20.0, 20.0)
        rOffset = random.uniform(-20.0, 20.0)
        spinTrack = LerpHprInterval(self.rotDummy, time, Vec3(hOffset, -3080 * time + offset, 90 + rOffset), startHpr=Vec3(hOffset, offset, 90 + rOffset))
        movement = Sequence(Func(self.motion_trail.beginTrail), Func(self.motion_trail2.beginTrail), throwTrack, Func(self.motion_trail.endTrail), Func(self.motion_trail2.endTrail))
        self.track = Sequence(Parallel(spinTrack, movement), Func(self.cleanUpEffect))

    def play(self, time, targetPos, motion_color=None, rate=1):
        self.createTrack(time, targetPos, motion_color)
        self.track.start()

    def cleanUpEffect(self):
        self.detachNode()
        if self.pool.isUsed(self):
            self.pool.checkin(self)

    def destroy(self):
        self.stop()
        self.motion_trail.destroy()
        self.motion_trail2.destroy()
        EffectController.destroy(self)
        PooledEffect.destroy(self)
# okay decompiling .\pirates\effects\DaggerProjectile.pyc
