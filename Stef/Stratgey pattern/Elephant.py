import abc
import random
from Pachyderm import *

class Elephant(Pachyderm):

    y = random.randint(1,2)
    Names = ""
    food = "Hay"
    def MakeNoise(self):
        print("Toot")

    def Roam(self):
        if (Elephant.y == 1):
            print ("Elephant roamed.")
        else:
            print ("Elephant did not roam.")

    def Eat(self):
        if(Elephant.y == 1):
            print ("Elephant ate.")
        else:
            print ("Elephant did not want to eat.")

    def Sleep(self):
        if(Elephant.y == 1):
            print ("Elephant is sleeping.")

        else:
            print ("Elephant did not want to sleep.")


    def WakeUp(self):
        if(Elephant.y == 1):
            print ("Elephant is awake.")
        else:
            print ("Elephant did not want to wake up.")
