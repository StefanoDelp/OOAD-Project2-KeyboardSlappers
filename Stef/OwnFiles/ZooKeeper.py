import abc
from Wolf import *
from Cat import *
from Dog import *
from Elephant import *
from Hippo import *
from Lion import *
from Rhino import *
from Tiger import *
class Zookeeper():
    Animals = []
    def Add(self , Animal):
        Zookeeper.Animals.append(Animal)
    
    def RollCall(self):
        print("Now Doing RollCall")
        for CurrentAnimal in Zookeeper.Animals:
            CurrentAnimal.MakeNoise()
    
    def WakeUp(self):
        print("Now Doing Wake Up")
        for CurrentAnimal in Zookeeper.Animals:
            CurrentAnimal.WakeUp()

    def Roam(self):
        print("Now Doing Roam")
        for CurrentAnimal in Zookeeper.Animals:
            CurrentAnimal.Roam()

    def Eat(self):
        print("Now Doing Eat")
        for CurrentAnimal in Zookeeper.Animals:
            CurrentAnimal.Eat()  

    def Sleep(self):
        print("Now Doing Sleep")
        for CurrentAnimal in Zookeeper.Animals:
            CurrentAnimal.WakeUp()