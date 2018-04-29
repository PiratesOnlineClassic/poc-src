from direct.distributed import DistributedSmoothNode
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from panda3d.core import *
from pirates.pirate import BattleNPCGameFSM
from pirates.piratesbase import PiratesGlobals


class NPCSkeletonGameFSM(BattleNPCGameFSM.BattleNPCGameFSM):

    def __init__(self, av):
        BattleNPCGameFSM.BattleNPCGameFSM.__init__(self, av)

    def cleanup(self):
        BattleNPCGameFSM.BattleNPCGameFSM.cleanup(self)