# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.ship.ShipInfo
from direct.distributed.DistributedObject import DistributedObject
from pirates.piratesbase import PiratesGlobals


class ShipInfo(DistributedObject):
    __module__ = __name__
    notify = directNotify.newCategory('ShipCrewMember')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.crewId = 0
        self.shipId = 0
        self.avatarId = 0
        self.hp = 0
        self.maxHp = 0
        self.locationName = 0
        self.activity = 0

    def announceGenerate(self):
        messenger.send(PiratesGlobals.CrewAddEvent, [self])
        DistributedObject.announceGenerate(self)

    def delete(self):
        messenger.send(PiratesGlobals.CrewRemoveEvent, [self])
        DistributedObject.delete(self)

    def getShipId(self):
        return self.shipId

    def setShipId(self, shipId):
        self.shipId = shipId

    def getAvatarId(self):
        return self.avatarId

    def setAvatarId(self, avatarId):
        self.avatarId = avatarId

    def isLocalAvatarsCaptain(self):
        return base.localAvatar.getCrewCaptainId() == self.avatarId

    def getName(self):
        return self.name

    def setName(self, avatarName):
        self.name = avatarName
        messenger.send(PiratesGlobals.CrewMemberNameChange, [self, avatarName])

    def getHp(self):
        return self.hp

    def setHp(self, hp):
        self.hp = hp
        messenger.send(PiratesGlobals.CrewMemberHpChange, [self, self.hp, self.maxHp])

    def getMaxHp(self):
        return self.maxHp

    def setMaxHp(self, maxHp):
        self.maxHp = maxHp
        messenger.send(PiratesGlobals.CrewMemberHpChange, [self, self.hp, self.maxHp])

    def getLocationName(self):
        return self.locationName

    def setLocationName(self, locationNameCode):
        self.locationName = locationNameCode

    def getActivity(self):
        return self.activity

    def setActivity(self, activityCode):
        self.activity = activityCode
# okay decompiling .\pirates\ship\ShipInfo.pyc
