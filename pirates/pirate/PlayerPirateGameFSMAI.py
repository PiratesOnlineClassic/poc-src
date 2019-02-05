from direct.directnotify.DirectNotifyGlobal import directNotify

from pirates.pirate.BattleAvatarGameFSMAI import BattleAvatarGameFSMAI
from pirates.uberdog.UberDogGlobals import InventoryType
from pirates.piratesbase import PiratesGlobals
from pirates.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from pirates.world.DistributedIslandAI import DistributedIslandAI
from pirates.world.DistributedGAInteriorAI import DistributedGAInteriorAI


class PlayerPirateGameFSMAI(BattleAvatarGameFSMAI):
    notify = directNotify.newCategory('PlayerPirateGameFSMAI')

    def __init__(self, air, avatar):
        BattleAvatarGameFSMAI.__init__(self, air, avatar)

    def enterLandRoam(self):
        self.avatar.startToonUp()

    def exitLandRoam(self):
        self.avatar.stopToonUp()

    def enterDeath(self):
        inventory = self.avatar.getInventory()
        if not inventory:
            self.notify.warning('Cannot teleport avatar %d, no inventory was found!' %
                self.avatar.doId)

            return

        area = self.avatar.getParentObj()
        if not area:
            self.notify.warning('Cannot teleport avatar %d to jail, no parent object found!' % (
                self.avatar.doId))

            return

        if not isinstance(area, DistributedIslandAI):
            self.notify.warning('Cannot teleport avatar %d to jail, parent has invalid type: %r!' % (
                self.avatar.doId, area))

            return

        instance = area.getParentObj()
        if not instance:
            self.notify.warning('Cannot teleport avatar %d to jail, parent object has no instance!' % (
                self.avatar.doId))

            return

        interior = area.getJailInterior()
        if not interior:
            self.notify.warning('Cannot teleport avatar %d to jail, unknown interior object!' % (
                self.avatar.doId))

            return

        # get a random cell door from the jails list of available cells,
        # ensure a cell doors was available...
        cellDoor = interior.getCellDoor()
        if not cellDoor:
            self.notify.warning('Cannot teleport avatar %d to jail, no cell doors found for interior %d!' % (
                self.avatar.doId, interior.doId))

            return

        # prepare this jail cell to be occupied by the avatar we
        # are sending to jail...
        cellDoor.setAvatarId(0)
        cellDoor.b_setHealth(cellDoor.getMaxHealth())
        self.avatar.setJailCellIndex(cellDoor.getCellIndex())

        # update the avatar's inventory values
        vitaeCost = (10 * 60) * 60
        inventory.b_setStackQuantity(InventoryType.Vitae_Level, 1)
        inventory.b_setStackQuantity(InventoryType.Vitae_Cost, vitaeCost)
        inventory.b_setStackQuantity(InventoryType.Vitae_Left, vitaeCost)
        self.avatar.b_setHp(1)

        # tell the instance to send the avatar to the jail, and set it's interest
        # properly before we update their game state...
        instance.d_sendLocalAvatarToJail(self.avatar.doId, interior.doId,
            interior.parentId, interior.zoneId)

    def exitDeath(self):
        pass

    def enterThrownInJail(self):
        area = self.avatar.getParentObj()
        if not area:
            self.notify.warning('Cannot finish teleporting to jail, avatar %d has no parent object!' % (
                self.avatar.doId))

            return

        if not isinstance(area, DistributedGAInteriorAI):
            self.notify.warning('Cannot finish teleporting avatar %d to jail, parent has invalid type: %r!' % (
                self.avatar.doId, area))

            return

        instance = area.getParentObj()
        if not instance:
            self.notify.warning('Cannot finish teleporting to jail, avatar %d parent object has no instance!' % (
                self.avatar.doId))

            return

        if not isinstance(instance, DistributedInstanceBaseAI):
            self.notify.warning('Cannot finish teleporting avatar %d to jail, parent instance has invalid type: %r!' % (
                self.avatar.doId, instance))

            return

        # retrieve the spawn position of the avatar's current cell index,
        # this is where the avatar will spawn in the jail cell...
        (x, y, z, h) = instance.getSpawnPt(area.getUniqueId(), self.avatar.getJailCellIndex())
        instance.d_setSpawnInfo(self.avatar.doId, x, y, z, h, 0, [area.doId,
            area.parentId, area.zoneId])

        # broadcast the avatar's current cell index to enable interaction with
        # the appropriate cell door...
        self.avatar.d_setJailCellIndex(self.avatar.getJailCellIndex())

    def exitThrownInJail(self):
        pass
