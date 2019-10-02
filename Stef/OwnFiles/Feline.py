import abc
import random
from Animal import *

class Feline(Animal):

    y = random.randint(1,2)
    #resp  = Response();
    def MakeNoise(self):
        print("Meow")

    #def setName(Name):
    #    Names = Name
    #    return Name

    def Roam(self):
        if (Feline.y == 1):
            return ("Feline roamed.")
        else:
            return ("Feline did not roam.")

    def Eat(self):
        if(Feline.y == 1):
            return ("Feline ate.")
        else:
            return ("Feline did not want to eat.")

    def Sleep(self):
        if(Feline.y == 1):
            return ("Feline is sleeping.")

        else:
            return ("Feline did not want to sleep.")


    def WakeUp(self):
        if(Feline.y == 1):
            return ("Feline is awake.")
        else:
            return ("Feline did not want to wake up.")
