# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.battle.Teamable


class Teamable:
    __module__ = __name__

    def __init__(self, team=-1, siege=0, pvp=0):
        self._team = team
        self._siegeTeam = siege
        self._pvpTeam = pvp

    def setTeam(self, team):
        self._team = team

    def getTeam(self):
        return self._team

    def setSiegeTeam(self, team):
        self._siegeTeam = team

    def getSiegeTeam(self):
        return self._siegeTeam

    def setPVPTeam(self, team):
        self._pvpTeam = team

    def getPVPTeam(self):
        return self._pvpTeam

    def isUndead(self):
        return False

    def b_setTeam(self, team):
        self.setTeam(team)
        self.sendUpdate('setTeam', [self._team])

    def b_setSiegeTeam(self, team):
        self.setSiegeTeam(team)
        self.sendUpdate('setSiegeTeam', [self._siegeTeam])

    def b_setPVPTeam(self, team):
        self.setPVPTeam(team)
        self.sendUpdate('setPVPTeam', [self._pvpTeam])

    def inPVP(self):
        if self.getPVPTeam() or self.getSiegeTeam() or self.isUndead():
            return True
        else:
            return False
# okay decompiling .\pirates\battle\Teamable.pyc
