import abc
from Wolf import *
from Cat import *
from Dog import *
from Elephant import *
from Hippo import *
from Lion import *
from Rhino import *
from Tiger import *

class ZooKeeper():
    Animals = []
    def Add(self , Animal):
        ZooKeeper.Animals.append(Animal)

    def RollCall(self):
        self.notify
        print("Now Doing RollCall")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.MakeNoise()
        self.cease

    def WakeUp(self):
        self.notify
        print("Now Doing Wake Up")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.WakeUp()
        self.cease

    def Roam(self):
        self.notify
        print("Now Doing Roam")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.Roam()
        self.cease

    def Eat(self):
        self.notify
        print("Now Doing Eat")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.Eat()
        self.cease

    def Sleep(self):
        self.notify
        print("Now Doing Sleep")
        for CurrentAnimal in ZooKeeper.Animals:
            CurrentAnimal.WakeUp()
        self.cease

    """
    This is where the observer pattern will be implemented
    """
    def __init__(self):
        self.observers = set()
    """
    Once the ZooKeeper completes his last task for the day,
    the ZooAnnouncer should cease observing and deconstruct.
    """
    def cease(self):
        for object in self.observers:
            object.close()
        del self.observers

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for object in self.observers:
            object.update()

"""
This is where the observer pattern will be implemented.
Example from the book "Python Essential Reference" involving observer pattern.
"""
class ZooAnnouncer(object):
    def __init__(self, announcemnet):
        self.announcement = announcement
        self.announcement.register(self)

    def unregister(self, observer):
        try:
            self.observers.remove(observer)
        except (KeyError, AttributeError):
            pass
    """
    The ZooAnnouncer will respond to this by telling the Zoo
    (issuing a print statement) something like “Hi, this is
    the Zoo Announcer.  The Zookeeper is about to wake the animals!”.
    (Note, this should not replace the text messages the ZooKeeper
    themselves may issue from the original flow.)
    """
    def update(self):
        if self.WakeUp:
            print("Hi, this is the Zoo Announcer. The Zookeeper is about to wake up the animals!")
        elif self.RollCall:
            print("Hi, this is the Zoo Announcer. The Zookeeper is about to do roll call!")
        elif self.Eat:
            print("Hi, this is the Zoo Announcer. The Zookeeper is about feed the animals!")
        elif self.Sleep:
            print("Hi, this is the Zoo Announcer. The Zookeeper is about to put the animals to sleep!")
        else:
            print("Hi, this is the Zoo Announcer. Can I please get your attention")
    """
    Once the ZooKeeper completes his last task for the day,
    the ZooAnnouncer should cease observing and deconstruct.
    """
    def close(self):
        print("That's all folks")

a = ZooKeeper()
one = ZooAnnouncer(a)
two = ZooAnnouncer(a)
a.WakeUp(one)
#a.withdraw(10)
