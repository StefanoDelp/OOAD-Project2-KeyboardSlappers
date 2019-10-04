import abc
import random
from Feline import *

class Cat(Feline):

    y = random.randint(1,2)

    Names = ""
    food = "kibble";
    #resp  = Response();
    def MakeNoise(self):
        print("Meow")

    def Roam(self):
        if (Cat.y == 1):
            print ("Cat roamed.")
        else:
            print ("Cat did not roam.")

    def Eat(self):
        if(Cat.y == 1):
            print ("Cat ate.")
        else:
            print ("Cat did not want to eat.")

    def Sleep(self):
        if(Cat.y == 1):
            print ("Cat is sleeping.")

        else:
            print ("Cat did not want to sleep.")


    def WakeUp(self):
        if(Cat.y == 1):
            return ("Cat is awake.")
        else:
            return ("Cat did not want to wake up.")
