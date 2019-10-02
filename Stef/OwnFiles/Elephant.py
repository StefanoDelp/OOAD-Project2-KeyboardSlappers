import abc
import random
from Pachyderm import *

class Elephant(Pachyderm):
    def Response():
        y = random.randint(1,2)
        return y
    Names = ""
    food = "Hay";
    resp  = Response();
    def makeNoise(self):
        print("Toot")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Response() == 1):
            return ("Elephant roamed.")
        else:
            return ("Elephant did not roam.")

    def eat(self):
        if(Response() == 1):
            return ("Elephant ate.")
        else:
            return ("Elephant did not want to eat.")

    def sleep(self):
        if(Response() == 1):
            return ("Elephant is sleeping.")

        else:
            return ("Elephant did not want to sleep.")


    def wakeUp(self):
        if(Response() == 1):
            return ("Elephant is awake.")
        else:
            return ("Elephant did not want to wake up.")
