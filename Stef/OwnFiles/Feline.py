import abc
import random
from Animal import *

class Feline(Animal):

    y = random.randint(1,2)
    def MakeNoise(self):
        print("Meow")

    def Roam(self):
        if (Feline.y == 1):
            print ("Feline roamed.")
        else:
            print ("Feline did not roam.")

    def Eat(self):
        if(Feline.y == 1):
            print ("Feline ate.")
        else:
            print ("Feline did not want to eat.")

    def Sleep(self):
        if(Feline.y == 1):
            print ("Feline is sleeping.")

        else:
            print ("Feline did not want to sleep.")


    def WakeUp(self):
        if(Feline.y == 1):
            print ("Feline is awake.")
        else:
            print ("Feline did not want to wake up.")
