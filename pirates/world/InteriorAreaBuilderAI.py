from direct.directnotify.DirectNotifyGlobal import directNotify
from pirates.world.GameAreaBuilderAI import GameAreaBuilderAI
from pirates.leveleditor import ObjectList
from pirates.piratesbase import PiratesGlobals
from pirates.world.DistributedCellDoorAI import DistributedCellDoorAI

class InteriorAreaBuilderAI(GameAreaBuilderAI):
    notify = directNotify.newCategory('InteriorAreaBuilderAI')

    def __init__(self, air, parent):
        GameAreaBuilderAI.__init__(self, air, parent)

        self.wantDoorLocatorNodes = config.GetBool('want-door-locator-nodes', True)
        self.wantJailCellDoors = config.GetBool('want-jail-cell-doors', True)

    def parentObjectToCell(self, object, zoneId=None, parent=None):
        parent = GameAreaBuilderAI.parentObjectToCell(self, object, zoneId, parent)
        object.b_setLocation(parent.doId, PiratesGlobals.InteriorDoorZone)

    def createObject(self, objType, objectData, parent, parentUid, objKey, dynamic, parentIsObj=False, fileName=None, actualParentObj=None):
        newObj = None

        if objType == ObjectList.DOOR_LOCATOR_NODE and self.wantDoorLocatorNodes:
            newObj = self.__createDoorLocatorNode(parent, parentUid, objKey, objectData)
        elif objType == 'Jail Cell Door' and self.wantJailCellDoors:
            newObj = self.__createCellDoor(parent, parentUid, objKey, objectData)
        else:
            newObj = GameAreaBuilderAI.createObject(self, objType, objectData, parent, parentUid, objKey,
                dynamic, parentIsObj, fileName, actualParentObj)

        return newObj

    def __createDoorLocatorNode(self, parent, parentUid, objKey, objectData):
        from pirates.world.DistributedInteriorDoorAI import DistributedInteriorDoorAI

        doorLocatorNode = DistributedInteriorDoorAI(self.air)
        doorLocatorNode.setUniqueId(objKey)
        doorLocatorNode.setPos(objectData.get('Pos', (0, 0, 0)))
        doorLocatorNode.setHpr(objectData.get('Hpr', (0, 0, 0)))
        doorLocatorNode.setScale(objectData.get('Scale', (1, 1, 1)))
        doorLocatorNode.setInteriorId(self.parent.doId, self.parent.parentId,
            self.parent.zoneId)

        if not self.parent.getInteriorFrontDoor():
            doorLocatorNode.setDoorIndex(0)
            self.parent.setInteriorFrontDoor(doorLocatorNode)
            exteriorDoor = self.parent.getExteriorFrontDoor()
        else:
            doorLocatorNode.setDoorIndex(1)
            self.parent.setInteriorBackDoor(doorLocatorNode)
            exteriorDoor = self.parent.getExteriorBackDoor()

        if not exteriorDoor:
            self.notify.debug('Cannot generate interior door %s, cant find other exterior door!' % (
                objKey))

            return

        exteriorWorld = self.parent.getParentObj()

        if not exteriorWorld:
            self.notify.debug('Cannot create interior door %s, for exterior with no parent!' % (
                objKey))

            return

        exterior = exteriorDoor.getParentObj()

        if not exterior:
            self.notify.debug('Cannot create interior door %s, no exterior found!' % (
                objKey))

            return

        doorLocatorNode.setBuildingUid(exteriorDoor.getBuildingUid())
        doorLocatorNode.setOtherDoor(exteriorDoor)
        doorLocatorNode.setExteriorId(exterior.doId, exteriorWorld.doId, exterior.zoneId)

        zoneId = self.parent.getZoneFromXYZ(doorLocatorNode.getPos())
        self.parent.generateChildWithRequired(doorLocatorNode, zoneId)
        self.parentObjectToCell(doorLocatorNode, zoneId)

        exteriorDoor.setOtherDoor(doorLocatorNode)

        self.addObject(doorLocatorNode)

        return doorLocatorNode

    def __createCellDoor(self, parent, parentUid, objKey, objectData):
        cellDoor = DistributedCellDoorAI(self.air)
        cellDoor.setUniqueId(objKey)
        cellDoor.setPos(objectData.get('Pos', (0, 0, 0)))
        cellDoor.setHpr(objectData.get('Hpr', (0, 0, 0)))
        cellDoor.setScale(objectData.get('Scale', (1, 1, 1)))
        cellDoor.setCellIndex(objectData.get('Cell Index', 0))

        self.setObjectTruePosHpr(cellDoor, objKey, parentUid, objectData)

        zoneId = self.parent.getZoneFromXYZ(cellDoor.getPos())
        self.parent.generateChildWithRequired(cellDoor, zoneId)
        self.parentObjectToCell(cellDoor, zoneId)

        self.addObject(cellDoor)

        return cellDoor
