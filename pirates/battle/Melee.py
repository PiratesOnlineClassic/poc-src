import Weapon
import WeaponGlobals
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from pirates.uberdog.UberDogGlobals import InventoryType

hitSfxs = None
missSfxs = None


def getHitSfx():
    global hitSfxs
    if not hitSfxs:
        hitSfxs = (
         loader.loadSfx('audio/swipeImpact-03.mp3'), loader.loadSfx('audio/swipeImpact-09.mp3'))
    return hitSfxs


def getMissSfx():
    global missSfxs
    if not missSfxs:
        missSfxs = (
         loader.loadSfx('audio/whoosh-10.mp3'), loader.loadSfx('audio/arm-Whoosh-05.mp3'))
    return missSfxs


class Melee(Weapon.Weapon):
    modelTypes = {InventoryType.MeleeWeaponL1: ('models/props/mrReid', Vec4(1, 1, 1, 1)), InventoryType.MeleeWeaponL2: ('models/props/mrReid', Vec4(1, 1, 1, 1)), InventoryType.MeleeWeaponL3: ('models/props/mrReid', Vec4(1, 1, 1, 1)), InventoryType.MeleeWeaponL4: ('models/props/mrReid', Vec4(1, 1, 1, 1)), InventoryType.MeleeWeaponL5: ('models/props/mrReid', Vec4(1, 1, 1, 1)), InventoryType.MeleeWeaponL6: ('models/props/mrReid', Vec4(1, 1, 1, 1))}
    vertex_list = [
     Vec4(0.0, 0.4, 0.0, 1.0), Vec4(0.0, 2.0, 0.0, 1.0), Vec4(-0.55, 2.95, 0.0, 1.0)]
    motion_color = [
     Vec4(0.1, 0.2, 0.4, 1.0), Vec4(0.1, 0.2, 0.4, 1.0), Vec4(0.1, 0.2, 0.4, 1.0)]
    neutralAnim = 'boxing_idle'
    walkAnim = 'walk'
    runAnim = 'run'
    strafeLeftAnim = 'strafe_left'
    strafeRightAnim = 'strafe_right'

    def __init__(self, itemId):
        Weapon.Weapon.__init__(self, itemId, 'melee')

    def getDrawIval(self, av, ammoSkillId=0, blendInT=0.1, blendOutT=0):
        track = Sequence(Func(self.attachTo, av), av.actorInterval('boxing_fromidle', blendInT=blendInT, blendOutT=blendOutT))
        return track

    def getReturnIval(self, av, blendInT=0.1, blendOutT=0.1):
        track = Sequence(av.actorInterval('boxing_fromidle', startFrame=8, endFrame=1, blendInT=blendInT, blendOutT=blendOutT), Func(self.detachFrom, av))
        return track

    @classmethod
    def setupSounds(cls):
        Melee.painAnim = 'boxing_hit_head_right'
        Melee.unsheathSfx = loader.loadSfx('audio/sword-unsheath.mp3')