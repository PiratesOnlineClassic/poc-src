from pirates.battle.BattleManagerBase import BattleManagerBase
from direct.directnotify import DirectNotifyGlobal
from pirates.battle import WeaponGlobals
from direct.distributed.ClockDelta import globalClockDelta

class BattleAttackerData(object):

    def __init__(self, battleManager):
        self._battleManager = battleManager

        self._avatar = None
        self._target = None

        self._skillId = 0
        self._ammoSkillId = 0

        self._reputation = 0
        self._gold = 0

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
        self._target = target

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        self._avatar = avatar

    @property
    def skillId(self):
        return self._skillId

    @skillId.setter
    def skillId(self, skillId):
        self._skillId = skillId

    @property
    def ammoSkillId(self):
        return self._ammoSkillId

    @ammoSkillId.setter
    def ammoSkillId(self, ammoSkillId):
        self._ammoSkillId = ammoSkillId

    @property
    def reputation(self):
        return self._reputation

    @reputation.setter
    def reputation(self, reputation):
        self._reputation = reputation

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, gold):
        self._gold = gold

    def destroy(self):
        self._target = None
        self._avatar = None

        self._skillId = 0
        self._ammoSkillId = 0

        self._reputation = 0
        self._gold = 0

class BattleTargetData(object):

    def __init__(self, battleManager):
        self._battleManager = battleManager

        self._avatar = None
        self._attackerData = {}

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        self._avatar = avatar

    @property
    def attackerData(self):
        return self._attackerData

    def hasAttackerData(self, attackerDoId):
        if not attackerDoId:
            return False

        return attackerDoId in self._attackerData

    def getAttackerData(self, attackerDoId):
        if not self.hasAttackerData(attackerDoId):
            return None

        return self._attackerData[attackerDoId]

    def addAttackerData(self, attackerDoId):
        if not attackerDoId:
            return

        avatar = self._battleManager.air.doId2do.get(attackerDoId)

        if not avatar:
            return

        if avatar.doId in self._attackerData:
            return

        attacker = BattleAttackerData(self._battleManager)
        attacker.avatar = avatar
        attacker.target = self

        self._attackerData[attacker.avatar.doId] = attacker

    def removeAttackerData(self, attackerData):
        if not attackerData:
            return

        if not isinstance(attackerData, BattleAttackerData):
            return

        if not attackerData.avatar:
            return

        if attackerData.avatar.doId not in self._attackerData:
            return

        del self._attackerData[attackerData.avatar.doId]
        attackerData.destroy()

    def destroy(self):
        self._target = None
        self._attackerData = {}

class BattleManagerAI(BattleManagerBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleManagerAI')

    def __init__(self, air):
        self.air = air
        self.enemySpawner = self.air.enemySpawner

        self.__updateTask = None
        self.__targetData = {}

    def startup(self):
        self.__updateTask = taskMgr.add(self.__update, '%s-update-task-%s' % (
            self.__class__.__name__, id(self)))

    def __update(self, task):
        for spawnType, spawnNodes in self.enemySpawner.spawnNodes.items():
            for spawnNode in spawnNodes:
                self.__checkEnemySpawnNode(spawnNode)

        return task.cont

    def hasTargetData(self, targetDoId):
        if not targetDoId:
            return False

        return targetDoId in self.__targetData

    def getTargetData(self, targetDoId):
        if not self.hasTargetData(targetDoId):
            return None

        return self.__targetData[targetDoId]

    def addTargetData(self, target, avatar):
        if not target:
            return

        if not avatar:
            return

        if self.hasTargetData(target.doId):
            return

        targetData = BattleTargetData(self)
        targetData.target = target
        targetData.addAttackerData(avatar.doId)

        self.__targetData[targetData.target.doId] = targetData

    def removeTargetData(self, targetData):
        if not targetData:
            return

        if not self.hasTargetData(targetData.target.doId):
            return

        targetData.destroy()
        del self.__targetData[targetData.target.doId]

    def targetInRange(self, attacker, target, skillId, ammoSkillId, pos):
        if not skillId or not ammoSkillId:
            return False

        tolerance = 0
        attackRange = self.getModifiedAttackRange(attacker, skillId, ammoSkillId)
        if attackRange == WeaponGlobals.INF_RANGE:
            return True

        distance = attacker.getDistance(target)
        if distance <= attackRange + tolerance:
            return True

        return False

    def useTargetedSkill(self, avatar, target, skillId, ammoSkillId, clientResult, areaIdList, timestamp, pos, charge):
        if not avatar:
            self.notify.debug('Cannot calculate targeted skill for unknown avatar!')
            return None

        if not target:
            self.notify.debug('Cannot calculate targeted skill for avatar %d, unknown target!' % (
                avatar.doId))

            return None

        if not self.hasTargetData(target.doId):
            self.addTargetData(target, avatar)

        skillResult = self.willWeaponHit(avatar, target, skillId,
            ammoSkillId, charge)

        timestamp = globalClockDelta.getRealNetworkTime(bits=32)
        distance = avatar.getDistance(target)

        attackerEffects, targetEffects = self.getModifiedSkillEffects(avatar, target,
            skillId, ammoSkillId, charge, distance)

        areaIdEffects = [
            attackerEffects,
            targetEffects
        ]

        targetData = self.getTargetData(target.doId)
        targetData.skillId = skillId
        targetData.ammoSkillId = ammoSkillId

        if not targetData:
            self.notify.warning('Cannot calculate targeted skill for avatar %d, no target data for target %d!' % (
                avatar.doId, target.doId))

            return None

        if not targetData.hasAttackerData(avatar.doId):
            targetData.addAttackerData(avatar.doId)

        attackerData = targetData.getAttackerData(avatar.doId)

        if not targetData:
            self.notify.warning('Cannot calculate targeted skill for avatar %d, no data for avatar!' % (
                avatar.doId))

            return None

        if skillResult == WeaponGlobals.RESULT_HIT:
            attackerData.reputation += self.getModifiedAttackReputation(avatar, target,
                skillId, ammoSkillId)

            attackerData.gold += 1

            self.__applyTargetEffects(target, targetEffects)
        elif skillResult == WeaponGlobals.RESULT_MISS:
            pass
        elif skillResult == WeaponGlobals.RESULT_DODGE:
            pass
        elif skillResult == WeaponGlobals.RESULT_PARRY:
            pass
        elif skillResult == WeaponGlobals.RESULT_RESIST:
            pass
        else:
            self.notify.debug('Cannot calculate targeted skill, unknown weapon skill result was found, %d!' % (
                skillResult))

            return None

        return [skillId, ammoSkillId, skillResult, target.doId, areaIdList, attackerEffects, targetEffects,
            areaIdEffects, timestamp, pos, charge]

    def __applyTargetEffects(self, target, targetEffects):
        if not target:
            self.notify.debug('Cannot apply target effects for unknown target!')
            return

        target.b_setHp(target.getHp()[0] + targetEffects[0])
        target.b_setPower(target.getPower() + targetEffects[1])
        target.b_setLuck(target.getLuck() + targetEffects[2])
        target.b_setMojo(target.getMojo() + targetEffects[3])
        target.b_setSwiftness(target.getSwiftness() + targetEffects[4])

    def __applyAttackerEffects(self, avatar, attackerEffects):
        if not target:
            self.notify.debug('Cannot apply attacker effects for unknown avatar!')
            return

        avatar.b_setHp(avatar.getHp()[0] + targetEffects[0])
        avatar.b_setPower(avatar.getPower() + targetEffects[1])
        avatar.b_setLuck(avatar.getLuck() + targetEffects[2])
        avatar.b_setMojo(avatar.getMojo() + targetEffects[3])
        avatar.b_setSwiftness(avatar.getSwiftness() + targetEffects[4])

    def __checkEnemySpawnNode(self, spawnNode):
        if not spawnNode:
            return

        if not spawnNode.npc:
            return

        targetData = self.getTargetData(spawnNode.npc.doId)

        if not targetData:
            return

        # TODO: FIXME!
        #for attackerData in list(targetData.attackerData.values()):
        #    avatar = attackerData.avatar
        #
        #    if not self.targetInRange(avatar, spawnNode.npc, attackerData.skillId, attackerData.ammoSkillId, avatar.getPos()):
        #        print ("Av out of range", avatar, spawnNode.npc, avatar.getPos())
        #        targetData.removeAttackerData(attackerData)

        if spawnNode.npc.getHp()[0] <= 0:
            self.__enemyDied(spawnNode, spawnNode.npc)
            return

        if not targetData.attackerData:
            self.removeTargetData(targetData)

    def __enemyDied(self, spawnNode, target):
        target = self.air.doId2do.get(target.doId)

        if not target:
            return

        if target.getIsKilled():
            return

        targetData = self.getTargetData(target.doId)

        if not targetData:
            return

        for attackerData in list(targetData.attackerData.values()):
            self.__giveAttackerReward(attackerData.avatar, target, attackerData.reputation,
                attackerData.gold)

            targetData.removeAttackerData(attackerData)

        self.removeTargetData(targetData)
        spawnNode.processDeath()

    def __giveAttackerReward(self, avatar, target, reputation, gold):
        inventory = self.air.inventoryManager.getInventory(avatar.doId)

        if not inventory:
            self.notify.debug('Cannot calculate targeted skill reward, unknown inventory for avatar %d!' %(
                avatar.doId))

            return

        inventory.setGeneralRep(inventory.getGeneralRep() + reputation)
        inventory.setGoldInPocket(inventory.getGoldInPocket() + gold)
