# uncompyle6 version 3.1.1
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)]
# Embedded file name: pirates.pirate.HumanAnimationMixer
from direct.directnotify import DirectNotifyGlobal
from pirates.pirate.BipedAnimationMixer import BipedAnimationMixer


class HumanAnimationMixer(BipedAnimationMixer):
    
    notify = DirectNotifyGlobal.directNotify.newCategory('HumanAnimationMixer')
# okay decompiling .\pirates\pirate\HumanAnimationMixer.pyc
