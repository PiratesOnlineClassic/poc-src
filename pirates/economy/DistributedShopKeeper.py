from direct.showbase.ShowBaseGlobal import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.uberdog.RejectCode import RejectCode
from otp.otpbase import OTPGlobals
from otp.otpgui import OTPDialog
from pirates.economy.EconomyGlobals import *
from pirates.distributed import InteractGlobals
from pirates.piratesbase import PiratesGlobals
from pirates.piratesgui import PiratesGuiGlobals
from pirates.economy import StoreGUI, AccessoriesStoreGUI, TattooStoreGUI, JewelryStoreGUI, BarberStoreGUI, MusicianGUI
from pirates.economy import ShipStoreGUI
from pirates.uberdog.UberDogGlobals import *
from pirates.uberdog.DistributedInventoryBase import DistributedInventoryBase
from direct.interval.IntervalGlobal import *
from pirates.piratesbase import PLocalizer
from pirates.piratesgui import PDialog
from pirates.pirate import AvatarTypes
from pirates.piratesgui.ShipShoppingPanel import ShipShoppingPanel
from pirates.economy.EconomyGlobals import *
from pirates.economy import EconomyGlobals
from pirates.ship.ShipGlobals import *
from pirates.leveleditor import NPCList
from pirates.makeapirate import ClothingGlobals

class DistributedShopKeeper:
    notify = directNotify.newCategory('DistributedShopKeeper')
    shopCoins = None
    barberCoin = None
    blacksmithCoin = None
    gunsmithCoin = None
    jewelerCoin = None
    shipwrightCoin = None
    tailorCoin = None
    tattooCoin = None
    gypsyCoin = None
    trainerCoin = None
    pvpRewardsCoin = None
    musicianCoin = None
    
    def __init__(self):
        self.shopInventory = []
        self.shopCoin = None
        self.shopCoinGlow = None
        self.__invRequest = None

    def generate(self):
        DistributedShopKeeper.notify.debug('generate(%s)' % self.doId)
        self.storeMenuGUI = None
        self.pickShipGUI = None
        self.confirmDialog = None
        self.fadeIval = None
        self.storeType = None

    def announceGenerate(self):
        DistributedShopKeeper.notify.debug('announceGenerate(%s)' % self.doId)
        self.loadShopCoin()
        if self.avatarType.isA(AvatarTypes.Cannoneer):
            self.shopInventory = CANNON_AMMO_SHELF_L1 + CANNON_AMMO_SHELF_L2 + CANNON_POUCH_SHELF
        elif self.avatarType.isA(AvatarTypes.Blacksmith):
            if base.config.GetBool('low-weapons-only', 0):
                self.shopInventory = MELEE_SHELF_L1 + MELEE_SHELF_L2 + DAGGER_AMMO_SHELF_L1 + DAGGER_AMMO_SHELF_L2 + DAGGER_POUCH_SHELF
            else:
                self.shopInventory = MELEE_SHELF_L1 + MELEE_SHELF_L2 + MELEE_SHELF_L3 + DAGGER_AMMO_SHELF_L1 + DAGGER_AMMO_SHELF_L2 + DAGGER_POUCH_SHELF
        elif self.avatarType.isA(AvatarTypes.Bartender):
            self.shopInventory = MELEE_SHELF_L1 + MISSILE_SHELF_L1 + BOMB_SHELF_L1
        elif self.avatarType.isA(AvatarTypes.Gunsmith):
            if base.config.GetBool('low-weapons-only', 0):
                self.shopInventory = MISSILE_SHELF_L1 + MISSILE_SHELF_L2 + PISTOL_AMMO_SHELF_L1 + PISTOL_AMMO_SHELF_L2 + PISTOL_POUCH_SHELF + BOMB_SHELF_L1 + BOMB_SHELF_L2 + BOMB_AMMO_SHELF_L1 + BOMB_AMMO_SHELF_L2 + GRENADE_POUCH_SHELF + CANNON_AMMO_SHELF_L1 + CANNON_AMMO_SHELF_L2 + CANNON_POUCH_SHELF
            else:
                self.shopInventory = MISSILE_SHELF_L1 + MISSILE_SHELF_L2 + MISSILE_SHELF_L3 + PISTOL_AMMO_SHELF_L1 + PISTOL_AMMO_SHELF_L2 + PISTOL_POUCH_SHELF + BOMB_SHELF_L1 + BOMB_SHELF_L2 + BOMB_SHELF_L3 + BOMB_AMMO_SHELF_L1 + BOMB_AMMO_SHELF_L2 + GRENADE_POUCH_SHELF + CANNON_AMMO_SHELF_L1 + CANNON_AMMO_SHELF_L2 + CANNON_POUCH_SHELF
        elif self.avatarType.isA(AvatarTypes.Grenadier):
            self.shopInventory = BOMB_SHELF_L1 + BOMB_SHELF_L2 + BOMB_SHELF_L3 + BOMB_AMMO_SHELF_L1 + BOMB_AMMO_SHELF_L2 + GRENADE_POUCH_SHELF
        elif self.avatarType.isA(AvatarTypes.Gypsy):
            if base.config.GetBool('low-weapons-only', 0):
                self.shopInventory = TONIC_SHELF_L1 + TONIC_SHELF_L2 + MOJO_SHELF_L1 + MOJO_SHELF_L2
            else:
                self.shopInventory = TONIC_SHELF_L1 + TONIC_SHELF_L2 + MOJO_SHELF_ALL
        elif self.avatarType.isA(AvatarTypes.Merchant):
            self.shopInventory = PISTOL_AMMO_SHELF_L1 + MELEE_SHELF_L1 + MISSILE_SHELF_L1
        elif self.avatarType.isA(AvatarTypes.MedicineMan):
            self.shopInventory = TONIC_SHELF_L1 + TONIC_SHELF_L2
        elif self.avatarType.isA(AvatarTypes.Musician):
            self.shopInventory = MUSIC_SHELF

    def loadShopCoin(self):
        if not DistributedShopKeeper.shopCoins:
            DistributedShopKeeper.shopCoins = loader.loadModel('models/textureCards/shopCoins')
        
        if not DistributedShopKeeper.barberCoin:
            DistributedShopKeeper.barberCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_barber')
        
        if not DistributedShopKeeper.blacksmithCoin:
            DistributedShopKeeper.blacksmithCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_blacksmith')
        
        if not DistributedShopKeeper.gunsmithCoin:
            DistributedShopKeeper.gunsmithCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_gunsmith')
        
        if not DistributedShopKeeper.jewelerCoin:
            DistributedShopKeeper.jewelerCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_jeweler')
        
        if not DistributedShopKeeper.shipwrightCoin:
            DistributedShopKeeper.shipwrightCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_shipwright')
        
        if not DistributedShopKeeper.tailorCoin:
            DistributedShopKeeper.tailorCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_tailor')
        
        if not DistributedShopKeeper.tattooCoin:
            DistributedShopKeeper.tattooCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_tattoo')
        
        if not DistributedShopKeeper.gypsyCoin:
            DistributedShopKeeper.gypsyCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_voodoo')
        
        if not DistributedShopKeeper.trainerCoin:
            DistributedShopKeeper.trainerCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_trainer')
        
        if not DistributedShopKeeper.pvpRewardsCoin:
            DistributedShopKeeper.pvpRewardsCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_jeweler')
        
        if not DistributedShopKeeper.musicianCoin:
            DistributedShopKeeper.musicianCoin = DistributedShopKeeper.shopCoins.find('**/shopCoin_music')
        
        if not self.shopCoin:
            if DistributedShopKeeper.shopCoins:
                if self.avatarType.isA(AvatarTypes.Barber):
                    tex = DistributedShopKeeper.barberCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Blacksmith):
                    tex = DistributedShopKeeper.blacksmithCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Gunsmith):
                    tex = DistributedShopKeeper.gunsmithCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Jeweler):
                    tex = DistributedShopKeeper.jewelerCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Shipwright):
                    tex = DistributedShopKeeper.shipwrightCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Tailor):
                    tex = DistributedShopKeeper.tailorCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Tattoo):
                    tex = DistributedShopKeeper.tattooCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Gypsy):
                    tex = DistributedShopKeeper.gypsyCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Musician):
                    tex = DistributedShopKeeper.musicianCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.Trainer):
                    tex = DistributedShopKeeper.trainerCoin.copyTo(self.nametag3d)
                elif self.avatarType.isA(AvatarTypes.PvPRewards):
                    tex = DistributedShopKeeper.pvpRewardsCoin.copyTo(self.nametag3d)
                else:
                    tex = None
                if tex:
                    self.shopCoin = tex
                    if self.nametagIcon:
                        self.shopCoin.setScale(2.0)
                        self.shopCoin.setPos(0.0, 0.0, 7.0)
                    else:
                        self.shopCoin.setScale(2.5)
                        self.shopCoin.setPos(0.0, 0.0, 3.5)
                    self.shopCoin.reparentTo(self.getNameText())
                    self.shopCoin.setDepthWrite(0)
                    self.shopCoinGlow = loader.loadModel('models/effects/lanternGlow')
                    self.shopCoinGlow.reparentTo(self.nametag.getNameIcon())
                    self.shopCoinGlow.setColorScaleOff()
                    self.shopCoinGlow.setFogOff()
                    self.shopCoinGlow.setLightOff()
                    if not self.nametagIcon:
                        self.shopCoinGlow.setScale(20.0)
                        self.shopCoinGlow.setPos(0, -0.05, 3.0)
                    else:
                        self.shopCoinGlow.setScale(15.0)
                        self.shopCoinGlow.setPos(0, -0.05, 6.5)
                    self.shopCoinGlow.setDepthWrite(0)
                    self.shopCoinGlow.node().setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
                    self.shopCoinGlow.setColor(0.85, 0.85, 0.85, 0.85)
        else:
            if self.nametagIcon:
                self.shopCoin.setScale(2.0)
                self.shopCoin.setPos(0.0, 0.0, 7.0)
            else:
                self.shopCoin.setScale(2.5)
                self.shopCoin.setPos(0.0, 0.0, 3.5)
            self.shopCoin.reparentTo(self.getNameText())
            self.shopCoinGlow.reparentTo(self.nametag.getNameIcon())
            if not self.nametagIcon:
                self.shopCoinGlow.setScale(20.0)
                self.shopCoinGlow.setPos(0, -0.05, 3.0)
            else:
                self.shopCoinGlow.setScale(15.0)
                self.shopCoinGlow.setPos(0, -0.05, 6.5)

    def disable(self):
        DistributedShopKeeper.notify.debug('disable(%s)' % self.doId)
        self.finishShopping()

    def delete(self):
        DistributedShopKeeper.notify.debug('delete(%s)' % self.doId)

    def startShopping(self, storeType):
        self.acceptOnce('exitStore', self.finishShopping)
        self.acceptOnce('makeSale', self.sendRequestMakeSale)
        self.acceptOnce('purchaseAccessories', self.sendRequestAccessories)
        self.acceptOnce('requestMusic', self.sendRequestMusic)
        self.storeType = storeType
        if storeType == InteractGlobals.STORE:
            inventory = self.shopInventory[:]
            if hasattr(self.cr.distributedDistrict, 'siegeManager') and self.cr.distributedDistrict.siegeManager.getPvpEnabled() and self.cr.distributedDistrict.siegeManager.getUseRepairKit() and self.avatarType.isA(AvatarTypes.Gunsmith):
                inventory += SIEGE_SHELF
            
            self.storeMenuGUI = StoreGUI.StoreGUI(inventory, PLocalizer.MerchantStore)
        elif storeType == InteractGlobals.MUSICIAN:
            self.fadeIval = Sequence(Func(self.setTransparency, 1.0), self.colorScaleInterval(1.0, VBase4(1.0, 1.0, 1.0, 0.0)), Func(self.hide))
            self.fadeIval.start()
            inventory = self.shopInventory[:]
            self.storeMenuGUI = MusicianGUI.MusicianGUI(inventory, PLocalizer.InteractMusician)
        elif storeType == InteractGlobals.SHIPS:
            self.storeMenuGUI = ShipStoreGUI.ShipStoreGUI(SHIP_SHELF, PLocalizer.Shipyard)
        elif storeType == InteractGlobals.TRAIN:
            pass
        elif storeType == InteractGlobals.UPGRADE:
            pass
        elif storeType == InteractGlobals.ACCESSORIES_STORE:
            self.fadeIval = Sequence(Func(self.setTransparency, 1.0), self.colorScaleInterval(1.0, VBase4(1.0, 1.0, 1.0, 0.0)), Func(self.hide))
            self.fadeIval.start()
            self.storeMenuGUI = AccessoriesStoreGUI.AccessoriesStoreGUI(npc = self, shopId = self.getShopId())
        elif storeType == InteractGlobals.TATTOO_STORE:
            self.fadeIval = Sequence(Func(self.setTransparency, 1.0), self.colorScaleInterval(1.0, VBase4(1.0, 1.0, 1.0, 0.0)), Func(self.hide))
            self.fadeIval.start()
            self.storeMenuGUI = TattooStoreGUI.TattooStoreGUI(npc = self, shopId = self.getShopId())
        elif storeType == InteractGlobals.JEWELRY_STORE:
            self.fadeIval = Sequence(Func(self.setTransparency, 1.0), self.colorScaleInterval(1.0, VBase4(1.0, 1.0, 1.0, 0.0)), Func(self.hide))
            self.fadeIval.start()
            self.storeMenuGUI = JewelryStoreGUI.JewelryStoreGUI(npc = self, shopId = self.getShopId())
        elif storeType == InteractGlobals.BARBER_STORE:
            self.fadeIval = Sequence(Func(self.setTransparency, 1.0), self.colorScaleInterval(1.0, VBase4(1.0, 1.0, 1.0, 0.0)), Func(self.hide))
            self.fadeIval.start()
            self.storeMenuGUI = BarberStoreGUI.BarberStoreGUI(npc = self, shopId = self.getShopId())
        elif storeType == InteractGlobals.PVP_REWARDS_TATTOO:
            self.fadeIval = Sequence(Func(self.setTransparency, 1.0), self.colorScaleInterval(1.0, VBase4(1.0, 1.0, 1.0, 0.0)), Func(self.hide))
            self.fadeIval.start()
            self.storeMenuGUI = TattooStoreGUI.TattooStoreGUI(npc = self, shopId = PiratesGlobals.PRIVATEER_TATTOOS)

    def finishShopping(self):
        self.ignore('exitStore')
        self.ignore('makeSale')
        self.ignore('purchaseAccessories')
        self.ignore('requestMusic')
        messenger.send('stoppedShopping')
        if self.__invRequest:
            DistributedInventoryBase.cancelGetInventory(self.__invRequest)
            self.__invRequest = None
        
        if self.storeMenuGUI:
            self.storeMenuGUI.destroy()
            self.storeMenuGUI = None
        
        if self.pickShipGUI:
            self.pickShipGUI.destroy()
            self.pickShipGUI = None
        
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None
        
        self.setColorScale(1, 1, 1, 1)
        self.setTransparency(0)
        self.show()
        if self.fadeIval:
            self.fadeIval.pause()
            self.fadeIval = None
    
    def sendRequestMakeSale(self, buying = [], selling = [], names = []):
        self.storeMenuGUI.hide()
        self.sendUpdate('requestMakeSale', [
            buying,
            selling,
            names])
        self.finishShopping()
    
    def sendRequestMusic(self, songId):
        self.storeMenuGUI.hide()
        self.sendUpdate('requestMusic', [
            songId])
        self.finishShopping()

    def sendRequestAccessoriesList(self, avId = None):
        if avId is None:
            avId = localAvatar.getDoId()
            self.sendUpdate('requestAccessoriesList', [
                avId])

    def sendRequestTattooList(self, avId = None):
        if avId is None:
            avId = localAvatar.getDoId()
            self.sendUpdate('requestTattooList', [
                avId])

    def sendRequestJewelryList(self, avId = None):
        if avId is None:
            avId = localAvatar.getDoId()
            self.sendUpdate('requestJewelryList', [
                avId])

    def responseClothingList(self, avId, accessories):
        if self.storeMenuGUI and accessories:
            self.storeMenuGUI.setWardrobe(accessories)
    
    def responseTattooList(self, avId, tattoos):
        if self.storeMenuGUI and tattoos:
            self.storeMenuGUI.setWardrobe(tattoos)

    def responseJewelryList(self, avId, jewelry):
        if self.storeMenuGUI and jewelry:
            self.storeMenuGUI.setWardrobe(jewelry)

    def sendRequestAccessoryEquip(self, accessory):
        self.sendUpdate('requestAccessoryEquip', [
            accessory])

    def sendRequestJewelryEquip(self, jewelry):
        self.sendUpdate('requestJewelryEquip', [
            jewelry])

    def sendRequestAccessories(self, purchases, selling):
        self.sendUpdate('requestAccessories', [
            purchases,
            selling])

    def sendRequestJewelry(self, purchases, selling):
        self.sendUpdate('requestJewelry', [
            purchases,
            selling])

    def sendRequestTattoo(self, purchases, selling, currencyType = 0):
        self.sendUpdate('requestTattoo', [
            purchases,
            selling,
            currencyType])

    def sendRequestTattooEquip(self, tattoos):
        self.sendUpdate('requestTattooEquip', [
            tattoos])

    def sendRequestBarber(self, idx, color):
        self.sendUpdate('requestBarber', [
            idx,
            color])

    def makeTattooResponse(self, tattoo, zone, success):
        if self.storeMenuGUI and success:
            self.storeMenuGUI.tattooPurchase(zone, tattoo)

    def makeBarberResponse(self, uid, color, success):
        if self.storeMenuGUI and success:
            self.storeMenuGUI.barberPurchase(uid, color)

    def responseShipRepair(self, shipDoId):
        if self.pickShipGUI:
            self.pickShipGUI.updateShip(shipDoId)
            if self.confirmDialog:
                self.confirmDialog.destroy()
                self.confirmDialog = None
            
            self.confirmDialog = PDialog.PDialog(text = PLocalizer.ShipRepaired, style = OTPDialog.Acknowledge, command = self.handleRepairAcknowledge)

    def handleRepairAcknowledge(self, choice):
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None

    def makeSaleResponse(self, result):
        if result == RejectCode.OVERFLOW:
            localAvatar.guiMgr.createWarning(PLocalizer.TradeCannotHoldWarning, PiratesGuiGlobals.TextFG6)
        elif result == RejectCode.TIMEOUT:
            localAvatar.guiMgr.createWarning(PLocalizer.TradeTimeoutWarning, PiratesGuiGlobals.TextFG6)
        elif result == 2:
            if self.storeMenuGUI:
                self.storeMenuGUI.updateBalance()
            
        elif result != 1:
            localAvatar.guiMgr.createWarning(PLocalizer.TradeFailedWarning, PiratesGuiGlobals.TextFG6)
        else:
            localAvatar.guiMgr.combatTray.skillTray.updateSkillTrayAmounts()
            localAvatar.guiMgr.combatTray.tonicButton.getBestTonic()
            localAvatar.guiMgr.weaponPage.updateTonics()

    def startRepair(self, storeType):
        self.pickShipGUI = ShipShoppingPanel(PLocalizer.ShipRepair, doneCallback = self.confirmRepairShip, mode = 'repair')
        for shipId in base.localAvatar.getInventory().getShipDoIdList():
            self.pickShipGUI.addOwnShip(shipId, self.confirmRepairShip)

    def confirmRepairShip(self, shipId = None):
        if not shipId:
            return
        
        shipOV = self.cr.getOwnerView(shipId)
        if not shipOV:
            return
        
        cost = ShipGlobals.getRepairCost(shipOV)
        r = Functor(self.sendRequestRepairShip, shipId)
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None
        
        self.confirmDialog = PDialog.PDialog(text = PLocalizer.RepairConfirmDialog % {
            'gold': cost}, style = OTPDialog.YesNo, command = r)

    def sendRequestRepairShip(self, shipId, choice):
        shipOV = self.cr.getOwnerView(shipId)
        if not shipOV:
            return
        
        cost = ShipGlobals.getRepairCost(shipOV)
        if choice == 1:
            inventory = base.localAvatar.getInventory()
            if inventory:
                if inventory.getStackQuantity(InventoryType.GoldInPocket) < cost:
                    base.localAvatar.guiMgr.createWarning(PLocalizer.NotEnoughMoneyWarning, PiratesGuiGlobals.TextFG6)
                    return
            
            self.sendUpdate('requestPurchaseRepair', [shipId])
        
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None

    def startSellShip(self, storeType):
        self.pickShipGUI = ShipShoppingPanel(PLocalizer.SellShip, doneCallback = self.confirmSellShip, mode = 'sell')
        
        def inventoryHere(inv):
            self._DistributedShopKeeper__invRequest = None
            if inv:
                for shipId in inv.getShipDoIdList():
                    self.pickShipGUI.addOwnShip(shipId, self.confirmSellShip)
                
            else:
                self.finishShopping()

        if self.__invRequest:
            DistributedInventoryBase.cancelGetInventory(self.__invRequest)
        
        self.__invRequest = DistributedInventoryBase.getInventory(localAvatar.getInventoryId(), inventoryHere)

    def confirmSellShip(self, shipId = None):
        if not shipId:
            return
        
        shipOV = self.cr.getOwnerView(shipId)
        if not shipOV:
            return
        
        if shipOV.state != 'Off':
            base.localAvatar.guiMgr.createWarning(PLocalizer.ShipNotInBottleWarning, PiratesGuiGlobals.TextFG6)
            return
        
        modelType = ShipGlobals.getModelClass(shipOV.shipClass)
        cost = EconomyGlobals.getItemCost(modelType) / 2
        r = Functor(self.doubleConfirmSellShip, shipId)
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None
        
        self.confirmDialog = PDialog.PDialog(text = PLocalizer.SellShipConfirmDialog % {
            'gold': cost}, style = OTPDialog.YesNo, command = r)

    def doubleConfirmSellShip(self, shipId, choice):
        r = Functor(self.sendRequestSellShip, shipId)
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None
        
        if choice == 1:
            self.confirmDialog = PDialog.PDialog(text = PLocalizer.SellShipAreYouSureDialog, style = OTPDialog.YesNo, command = r)

    def sendRequestSellShip(self, shipId, choice):
        shipOV = self.cr.getOwnerView(shipId)
        if not shipOV:
            if self.pickShipGUI:
                self.pickShipGUI.hide()
            
            return
        
        modelType = ShipGlobals.getModelClass(shipOV.shipClass)
        cost = EconomyGlobals.getItemCost(modelType) / 2
        if choice == 1:
            inventory = base.localAvatar.getInventory()
            if inventory:
                if cost > 0 and inventory.getStackQuantity(InventoryType.GoldInPocket) + cost > inventory.getStackLimit(InventoryType.GoldInPocket):
                    r = Functor(self.sendRequestSellShipGoldOverflow, shipId)
                    if self.confirmDialog:
                        self.confirmDialog.destroy()
                        self.confirmDialog = None
                    
                    self.confirmDialog = PDialog.PDialog(text = PLocalizer.ExcessGoldLost, style = OTPDialog.YesNo, command = r)
                    return

            self.sendUpdate('requestSellShip', [shipId])
        
        if self.pickShipGUI:
            self.pickShipGUI.hide()
        
        self.finishShopping()
    
    def sendRequestSellShipGoldOverflow(self, shipId, choice):
        if self.pickShipGUI:
            self.pickShipGUI.hide()
        
        if choice == 1:
            self.sendUpdate('requestSellShip', [shipId])
        
        self.finishShopping()

    def startOverhaul(self, storeType):
        self.pickShipGUI = ShipShoppingPanel(PLocalizer.ShipOverhaul, doneCallback = self.confirmOverhaulShip, mode = 'overhaul')
        for shipId in base.localAvatar.getInventory().getShipDoIdList():
            self.pickShipGUI.addOwnShip(shipId, self.confirmOverhaulShip)
    
    def confirmOverhaulShip(self, shipId = None):
        if not shipId:
            return
        
        shipOV = self.cr.getOwnerView(shipId)
        if not shipOV:
            return
        
        if shipOV.state != 'Off':
            base.localAvatar.guiMgr.createWarning(PLocalizer.ShipNotInBottleWarning, PiratesGuiGlobals.TextFG6)
            return
        
        shipClass = shipOV.getShipClass()
        cost = EconomyGlobals.getItemCost(shipClass) * EconomyGlobals.OVERHAUL_COST_PERCENTAGE
        if self.confirmDialog:
            self.confirmDialog.destroy()
            self.confirmDialog = None
        
        self.confirmDialog = PDialog.PDialog(text = PLocalizer.OverhaulConfirmDialog % {
            'gold': cost}, style = OTPDialog.YesNo, command = self.sendRequestOverhaulShip, extraArgs = [shipId])
    
    def sendRequestOverhaulShip(self, choice, extraArgs):
        if self.pickShipGUI:
            self.pickShipGUI.hide()
        
        shipId = extraArgs[0]
        shipOV = self.cr.getOwnerView(shipId)
        if not shipOV:
            return
        
        shipClass = shipOV.getShipClass()
        cost = EconomyGlobals.getItemCost(shipClass) * EconomyGlobals.OVERHAUL_COST_PERCENTAGE
        if choice == 1:
            inventory = base.localAvatar.getInventory()
            if inventory:
                if inventory.getStackQuantity(InventoryType.GoldInPocket) < cost:
                    base.localAvatar.guiMgr.createWarning(PLocalizer.NotEnoughMoneyWarning, PiratesGuiGlobals.TextFG6)
                    return

            self.sendUpdate('requestPurchaseOverhaul', [shipId])
        
        self.finishShopping()


