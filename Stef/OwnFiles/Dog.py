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
            print ("Dog roamed.")
        else:
            print ("Dog did not roam.")

    def Eat(self):
        if(Dog.y == 1):
            print ("Dog ate.")
        else:
            print ("Dog did not want to eat.")

    def Sleep(self):
        if(Dog.y == 1):
            print ("Dog is sleeping.")

        else:
            print ("Dog did not want to sleep.")


    def WakeUp(self):
        if(Dog.y == 1):
            print ("Dog is awake.")
        else:
            print ("Dog did not want to wake up.")
