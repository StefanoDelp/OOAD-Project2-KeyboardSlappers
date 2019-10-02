import abc
import random
from Animal import *

class Feline(Animal):
    def Response():
        y = random.randint(1,2)
        return y
    resp  = Response();
    def makeNoise(self):
        print("Meow")

    def setName(Name):
        Names = Name
        return Name

    def roam():
        if (Response() == 1):
            return ("Feline roamed.")
        else:
            return ("Feline did not roam.")

    def eat():
        if(Response() == 1):
            return ("Feline ate.")
        else:
            return ("Feline did not want to eat.")

    def sleep():
        if(Response() == 1):
            return ("Feline is sleeping.")

        else:
            return ("Feline did not want to sleep.")


    def wakeUp():
        if(Response() == 1):
            return ("Feline is awake.")
        else:
            return ("Feline did not want to wake up.")
