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


class Zoo():
    def main(self):
        WillieWolf = Wolf()
        WhinnyWolf = Wolf()
        CarlCat = Cat()
        CindyCat = Cat()
        DougDog = Dog()
        DippyDog = Dog()
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
        ZaneZooKeeper = ZooKeeper()
        ZaneZooKeeper.Add(WillieWolf)
        ZaneZooKeeper.Add(WhinnyWolf)
        ZaneZooKeeper.Add(CarlCat)
        ZaneZooKeeper.Add(CindyCat)
        ZaneZooKeeper.Add(DougDog)
        ZaneZooKeeper.Add(DippyDog)
        ZaneZooKeeper.Add(EllyElephant)
        ZaneZooKeeper.Add(EarlElephant)
        ZaneZooKeeper.Add(HarryHippo)
        ZaneZooKeeper.Add(HenryHippo)
        ZaneZooKeeper.Add(LillyLion)
        ZaneZooKeeper.Add(LarryLion)
        ZaneZooKeeper.Add(RyanRhino)
        ZaneZooKeeper.Add(RandyRhino)
        ZaneZooKeeper.Add(TonyTiger)
        ZaneZooKeeper.Add(TimmyTiger)
        ZaneZooKeeper.WakeUp()
        ZaneZooKeeper.RollCall()
        ZaneZooKeeper.Roam()
        ZaneZooKeeper.Eat()
        ZaneZooKeeper.Sleep()










        


if __name__ == '__main__':
    SlappingZoo = Zoo()
    SlappingZoo.main()
    
