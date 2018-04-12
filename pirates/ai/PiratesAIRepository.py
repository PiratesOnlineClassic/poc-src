import time
import random
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.distributed.PiratesInternalRepository import PiratesInternalRepository
from otp.distributed.OtpDoGlobals import *
from otp.friends.FriendManagerAI import FriendManagerAI
from pirates.piratesbase import PiratesGlobals
from pirates.distributed.PiratesDistrictAI import PiratesDistrictAI
from pirates.world import WorldGlobals
from pirates.ai.NewsManagerAI import NewsManagerAI
from pirates.piratesbase.UniqueIdManager import UniqueIdManager
from pirates.distributed.DistributedPopulationTrackerAI import DistributedPopulationTrackerAI
from otp.ai.MagicWordManagerAI import MagicWordManagerAI
from otp.ai.TimeManagerAI import TimeManagerAI
from pirates.instance.DistributedTeleportMgrAI import DistributedTeleportMgrAI
from pirates.piratesbase.DistributedTimeOfDayManagerAI import DistributedTimeOfDayManagerAI
from pirates.distributed.TargetManagerAI import TargetManagerAI
from pirates.battle.DistributedEnemySpawnerAI import DistributedEnemySpawnerAI
from pirates.trades.TradeManagerAI import TradeManagerAI
from pirates.world.WorldCreatorAI import WorldCreatorAI
from pirates.battle.BattleManagerAI import BattleManagerAI

class PiratesAIRepository(PiratesInternalRepository):
    notify = directNotify.newCategory('PiratesAIRepository')
    notify.setInfo(True)

    def __init__(self, baseChannel, serverId, districtName):
        PiratesInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='AI')

        self.districtName = districtName
        self.zoneAllocator = UniqueIdAllocator(PiratesGlobals.DynamicZonesBegin, PiratesGlobals.DynamicZonesEnd)
        self.zoneId2owner = {}
        self.uidMgr = UniqueIdManager(self)

    def handleConnected(self):
        PiratesInternalRepository.handleConnected(self)
        self.districtId = self.allocateChannel()
        self.distributedDistrict = PiratesDistrictAI(self)
        self.distributedDistrict.setName(self.districtName)
        self.distributedDistrict.setMainWorld(WorldGlobals.PiratesWorldSceneFile)
        self.distributedDistrict.generateWithRequiredAndId(self.districtId,
            self.getGameDoId(), 2)

        self.setAI(self.districtId, self.ourChannel)

        self.createGlobals()
        self.createWorlds()

        self.distributedDistrict.b_setAvailable(1)
        self.notify.info('District (%s) is now ready.' % self.districtName)
        messenger.send('district-ready')

    def incrementPopulation(self):
        self.populationTracker.b_setPopulation(self.populationTracker.getPopulation() + 1)

    def decrementPopulation(self):
        self.populationTracker.b_setPopulation(self.populationTracker.getPopulation() - 1)

    def allocateZone(self, owner=None):
        zoneId = self.zoneAllocator.allocate()
        if owner:
            self.zoneId2owner[zoneId] = owner

        return zoneId

    def deallocateZone(self, zone):
        if self.zoneId2owner.get(zone):
            del self.zoneId2owner[zone]

        self.zoneAllocator.free(zone)

    def getAvatarExitEvent(self, avId):
        return 'distObjDelete-%d' % avId

    def createGlobals(self):
        """
        Create "global" objects, e.g. TimeManager et al.
        """

        self.centralLogger = self.generateGlobalObject(OTP_DO_ID_CENTRAL_LOGGER, 'CentralLogger')

        self.populationTracker = DistributedPopulationTrackerAI(self)
        self.populationTracker.setShardId(self.districtId)
        self.populationTracker.setPopLimits(config.GetInt('shard-pop-limit-low', 100), config.GetInt('shard-pop-limit-high', 300))
        self.populationTracker.generateWithRequiredAndId(self.allocateChannel(), self.getGameDoId(), OTP_ZONE_ID_DISTRICTS_STATS)

        self.timeManager = TimeManagerAI(self)
        self.timeManager.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.travelAgent = self.generateGlobalObject(OTP_DO_ID_PIRATES_TRAVEL_AGENT, 'DistributedTravelAgent')

        self.teleportMgr = DistributedTeleportMgrAI(self)
        self.teleportMgr.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.timeOfDayMgr = DistributedTimeOfDayManagerAI(self)
        self.timeOfDayMgr.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.newsManager = NewsManagerAI(self)
        self.newsManager.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.friendManager = FriendManagerAI(self)
        self.friendManager.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.targetMgr = TargetManagerAI(self)
        self.targetMgr.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.enemySpawner = DistributedEnemySpawnerAI(self)
        self.enemySpawner.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.battleMgr = BattleManagerAI(self)
        self.battleMgr.startup()

        self.inventoryManager = self.generateGlobalObject(OTP_DO_ID_PIRATES_INVENTORY_MANAGER, 'DistributedInventoryManager')

        self.magicWords = MagicWordManagerAI(self)
        self.magicWords.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.tradeMgr = TradeManagerAI(self)
        self.tradeMgr.generateWithRequired(OTP_ZONE_ID_MANAGEMENT)

        self.guildManager = self.generateGlobalObject(OTP_DO_ID_PIRATES_GUILD_MANAGER, 'PCGuildManager')

    def createWorlds(self):
        """
        Create "worlds" objects, e.g. DistributedInstanceBase, DistributedOceanGrid et al.
        """

        self.worldCreator = WorldCreatorAI(self)
        self.worldCreator.loadObjectsFromFile(WorldGlobals.PiratesWorldSceneFile)
