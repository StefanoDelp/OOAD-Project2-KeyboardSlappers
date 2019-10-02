import abc
import random
from Animal import *

class Feline(Animal):

    y = random.randint(1,2)
    #resp  = Response();
    def makeNoise(self):
        print("Meow")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Feline.y == 1):
            return ("Feline roamed.")
        else:
            return ("Feline did not roam.")

    def eat(self):
        if(Feline.y == 1):
            return ("Feline ate.")
        else:
            return ("Feline did not want to eat.")

    def sleep(self):
        if(Feline.y == 1):
            return ("Feline is sleeping.")

        else:
            return ("Feline did not want to sleep.")


    def wakeUp(self):
        if(Feline.y == 1):
            return ("Feline is awake.")
        else:
            return ("Feline did not want to wake up.")
