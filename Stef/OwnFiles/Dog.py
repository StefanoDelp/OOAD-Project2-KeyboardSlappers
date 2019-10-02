import abc
import random
from Canine import *

class Dog(Canine):

    y = random.randint(1,2)
    Names = ""
    food = "Dog Bites";
    #resp  = Response();
    def makeNoise(self):
        print("Woof,Ruff")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Dog.y == 1):
            return ("Dog roamed.")
        else:
            return ("Dog did not roam.")

    def eat(self):
        if(Dog.y == 1):
            return ("Dog ate.")
        else:
            return ("Dog did not want to eat.")

    def sleep(self):
        if(Dog.y == 1):
            return ("Dog is sleeping.")

        else:
            return ("Dog did not want to sleep.")


    def wakeUp(self):
        if(Dog.y == 1):
            return ("Dog is awake.")
        else:
            return ("Dog did not want to wake up.")
