import abc
import random
from Canine import *

class Dog(Canine):
    def Response():
        y = random.randint(1,2)
        return y
    Names = ""
    food = "Dog Bites";
    resp  = Response();
    def makeNoise(self):
        print("Woof,Ruff")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Response() == 1):
            return ("Dog roamed.")
        else:
            return ("Dog did not roam.")

    def eat(self):
        if(Response() == 1):
            return ("Dog ate.")
        else:
            return ("Dog did not want to eat.")

    def sleep(self):
        if(Response() == 1):
            return ("Dog is sleeping.")

        else:
            return ("Dog did not want to sleep.")


    def wakeUp(self):
        if(Response() == 1):
            return ("Dog is awake.")
        else:
            return ("Dog did not want to wake up.")
