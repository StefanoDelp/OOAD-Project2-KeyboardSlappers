import abc
import random
from Feline import *

class Cat(Feline):
    def Response():
        y = random.randint(1,2)
        return y
    Names = ""
    food = "kibble";
    resp  = Response();
    def makeNoise(self):
        print("Meow")

    def setName(Name):
        Names = Name
        return Name

    def roam():
        if (Response() == 1):
            return ("Cat roamed.")
        else:
            return ("Cat did not roam.")

    def eat():
        if(Response() == 1):
            return ("Cat ate.")
        else:
            return ("Cat did not want to eat.")

    def sleep():
        if(Response() == 1):
            return ("Cat is sleeping.")

        else:
            return ("Cat did not want to sleep.")


    def wakeUp():
        if(Response() == 1):
            return ("Cat is awake.")
        else:
            return ("Cat did not want to wake up.")