import abc
from ZooAnnouncer import Subject,Observer
from typing import List

##Making the class obsevable
class ZooKeeper(Subject):
    Animals = []
    _state: int = None
    _observers: List[Observer] = []
    ## attachs new methods to be watched 
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    ## attachs new methods to be watched 
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
        The subscription management methods.
    """

    ## notifys when there is a change of status
    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.update(self)


    def Add(self , Animal):
        ZooKeeper.Animals.append(Animal)
    
    ## sets status and notifys
    def RollCall(self):
        self._state = 2
        self.notify()
        print("Now Doing RollCall")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.MakeNoise()
    ## sets status and notifys
    def WakeUp(self):
        self._state = 1
        self.notify()
        print("Now Doing Wake Up")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.WakeUp()
## sets status and notifys
    def Roam(self):
        self._state = 3
        self.notify()
        print("Now Doing Roam")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.Roam()
## sets status and notifys
    def Eat(self):
        self._state = 4
        self.notify()
        print("Now Doing Eat")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.Eat()  
## sets status and notifys
    def Sleep(self):
        self._state = 5
        self.notify()
        print("Now Doing Sleep")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.Sleep()