import abc
import random
from Canine import *

class Dog(Canine):

    y = random.randint(1,2)
    Names = ""
    food = "Dog Bites"
    def MakeNoise(self):
        print("Woof,Ruff")

    def Roam(self):
        if (Dog.y == 1):
            return ("Dog roamed.")
        else:
            return ("Dog did not roam.")

    def Eat(self):
        if(Dog.y == 1):
            return ("Dog ate.")
        else:
            return ("Dog did not want to eat.")

    def Sleep(self):
        if(Dog.y == 1):
            return ("Dog is sleeping.")

        else:
            return ("Dog did not want to sleep.")


    def WakeUp(self):
        if(Dog.y == 1):
            return ("Dog is awake.")
        else:
            return ("Dog did not want to wake up.")
