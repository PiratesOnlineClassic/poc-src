from pirates.uberdog.DistributedInventoryAI import DistributedInventoryAI
from direct.directnotify import DirectNotifyGlobal
from pirates.uberdog.UberDogGlobals import InventoryId, InventoryType, InventoryCategory
from pirates.reputation import ReputationGlobals

class PirateInventoryAI(DistributedInventoryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('PirateInventoryAI')

    def setReputation(self, repType, quantity, repAccType=None):
        avatar = self.air.doId2do.get(self.ownerId)

        if not avatar:
            self.notify.debug('Failed to set general rep for avatar %d, not found!' % (
                avatar.doId))

            return

        oldLevel, oldReputation = ReputationGlobals.getLevelFromTotalReputation(
            repType, self.getReputation(repType))

        newLevel, newReputation = ReputationGlobals.getLevelFromTotalReputation(
            repType, quantity)

        if repType == InventoryType.OverallRep or repType == InventoryType.GeneralRep:
            if newLevel > avatar.getLevel():
                avatar.b_setLevel(newLevel)
                avatar.d_levelUpMsg(repType, newLevel, 0)
        else:
            if newLevel > oldLevel:
                avatar.d_levelUpMsg(repType, newLevel, 0)

        self.b_setAccumulator(repAccType or repType, quantity)

    def getReputation(self, repType):
        return self.getItem(self.getAccumulator, repType)

    def setGeneralRep(self, quantity):
        self.setReputation(InventoryType.OverallRep, quantity, InventoryType.GeneralRep)

    def getGeneralRep(self):
        return self.getReputation(InventoryType.GeneralRep)

    def setGoldInPocket(self, quantity):
        self.b_setStack(InventoryType.GoldInPocket, quantity)

    def getGoldInPocket(self):
        return self.getItem(self.getStack, InventoryType.GoldInPocket)
