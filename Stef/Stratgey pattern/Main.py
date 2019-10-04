
from ZooAnnouncer import *
from ZooKeeper import *
import abc
from Wolf import *
from Cat import *
from Dog import *
from Elephant import *
from Hippo import *
from Lion import *
from Rhino import *
from Tiger import *

if __name__ == "__main__":
    # The client code.

    ## setting with stragey pattern
    WillieWolf = Wolf(FeedWithFear())
    WhinnyWolf = Wolf(FeedWithFear())
    
    CarlCat = Cat()
    CindyCat = Cat()
    ## setting with stragey pattern
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

    ZaneZooKeeper = ZooKeeper()

    WakeObserver = ObserverWakeUp()
    ZaneZooKeeper.attach(WakeObserver)

    RollCallObserver = ObserverRollCall()
    ZaneZooKeeper.attach(RollCallObserver)

    RoamCallObserver = ObserverRoam()
    ZaneZooKeeper.attach(RoamCallObserver)

    EatObserver = ObserverEat()
    ZaneZooKeeper.attach(EatObserver)

    SleepObserver = ObserverSleep()
    ZaneZooKeeper.attach(SleepObserver)

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