import abc
import random
from Pachyderm import *

class Rhino(Pachyderm):
    
    y = random.randint(1,2)
    Names = ""
    food = "Grass"
    def MakeNoise(self):
        print("Rhino Growl")

    #def setName(Name):
    #    Names = Name
    #    return Name

    def Roam(self):
        if (Rhino.y == 1):
            return ("Rhino roamed.")
        else:
            return ("Rhino did not roam.")

    def Eat(self):
        if(Rhino.y == 1):
            return ("Rhino ate.")
        else:
            return ("Rhino did not want to eat.")

    def Sleep(self):
        if(Rhino.y == 1):
            return ("Rhino is sleeping.")

        else:
            return ("Rhino did not want to sleep.")


    def WakeUp(self):
        if(Rhino.y == 1):
            return ("Rhino is awake.")
        else:
            return ("Rhino did not want to wake up.")
