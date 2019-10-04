"""

No longer used has been moved into main.py


import abc
from Wolf import *
from Cat import *
from Dog import *
from Elephant import *
from Hippo import *
from Lion import *
from Rhino import *
from Tiger import *
from ZooKeeper import * 
from Animal2 import *



class Zoo():
    def main(self, ZooKeeper):
        WillieWolf = Wolf(FeedWithFear())
        WhinnyWolf = Wolf(FeedWithFear())
        CarlCat = Cat()
        CindyCat = Cat()
        DougDog = Dog(FeedWithCare())
        DippyDog = Dog(FeedWithCare())
        EllyElephant = Elephant()
        EarlElephant = Elephant()
        HarryHippo = Hippo()
        HenryHippo = Hippo()
        LillyLion = Lion()
        LarryLion = Lion()
        RyanRhino = Rhino()
        RandyRhino = Rhino()
        TonyTiger = Tiger()
        TimmyTiger = Tiger()
        ZooKeeper.Add(WillieWolf)
        ZooKeeper.Add(WhinnyWolf)
        ZooKeeper.Add(CarlCat)
        ZooKeeper.Add(CindyCat)
        ZooKeeper.Add(DougDog)
        ZooKeeper.Add(DippyDog)
        ZooKeeper.Add(EllyElephant)
        ZooKeeper.Add(EarlElephant)
        ZooKeeper.Add(HarryHippo)
        ZooKeeper.Add(HenryHippo)
        ZooKeeper.Add(LillyLion)
        ZooKeeper.Add(LarryLion)
        ZooKeeper.Add(RyanRhino)
        ZooKeeper.Add(RandyRhino)
        ZooKeeper.Add(TonyTiger)
        ZooKeeper.Add(TimmyTiger)
        ZooKeeper.WakeUp()
        ZooKeeper.RollCall()
        ZooKeeper.Roam()
        ZooKeeper.Eat()
        ZooKeeper.Sleep()
"""

    
