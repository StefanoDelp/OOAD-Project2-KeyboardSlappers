import abc
import random
from Pachyderm import *

class Elephant(Pachyderm):

    y = random.randint(1,2)
    Names = ""
    food = "Hay"
    def MakeNoise(self):
        print("Toot")

    ###def setName(Name):
    ###    Names = Name
    ###    return Name

    def Roam(self):
        if (Elephant.y == 1):
            return ("Elephant roamed.")
        else:
            return ("Elephant did not roam.")

    def Eat(self):
        if(Elephant.y == 1):
            return ("Elephant ate.")
        else:
            return ("Elephant did not want to eat.")

    def Sleep(self):
        if(Elephant.y == 1):
            return ("Elephant is sleeping.")

        else:
            return ("Elephant did not want to sleep.")


    def WakeUp(self):
        if(Elephant.y == 1):
            return ("Elephant is awake.")
        else:
            return ("Elephant did not want to wake up.")
