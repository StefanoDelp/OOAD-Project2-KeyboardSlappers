import abc
import random
from Pachyderm import *

class Rhino(Pachyderm):
    def Response():
        y = random.randint(1,2)
        return y
    Names = ""
    food = "Grass";
    resp  = Response();
    def makeNoise(self):
        print("Rhino Growl")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Response() == 1):
            return ("Rhino roamed.")
        else:
            return ("Rhino did not roam.")

    def eat(self):
        if(Response() == 1):
            return ("Rhino ate.")
        else:
            return ("Rhino did not want to eat.")

    def sleep(self):
        if(Response() == 1):
            return ("Rhino is sleeping.")

        else:
            return ("Rhino did not want to sleep.")


    def wakeUp(self):
        if(Response() == 1):
            return ("Rhino is awake.")
        else:
            return ("Rhino did not want to wake up.")
