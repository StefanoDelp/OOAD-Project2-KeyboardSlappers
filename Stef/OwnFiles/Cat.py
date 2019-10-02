import abc
import random
from Feline import *

class Cat(Feline):

    y = random.randint(1,2)

    Names = ""
    food = "kibble";
    #resp  = Response();
    def makeNoise(self):
        print("Meow")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Cat.y == 1):
            return ("Cat roamed.")
        else:
            return ("Cat did not roam.")

    def eat(self):
        if(Cat.y == 1):
            return ("Cat ate.")
        else:
            return ("Cat did not want to eat.")

    def sleep(self):
        if(Cat.y == 1):
            return ("Cat is sleeping.")

        else:
            return ("Cat did not want to sleep.")


    def wakeUp(self):
        if(Cat.py == 1):
            return ("Cat is awake.")
        else:
            return ("Cat did not want to wake up.")
