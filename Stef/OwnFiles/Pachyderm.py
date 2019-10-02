import abc
import random
from Animal import *

class Pachyderm(Animal):

    y = random.randint(1,2)
    #resp  = Response();
    def makeNoise(self):
        print("Stomp")

    def setName(Name):
        Names = Name
        return Name

    def roam(self):
        if (Pachyderm.y == 1):
            return ("Pachyderm roamed.")
        else:
            return ("Pachyderm did not roam.")

    def eat(self):
        if(Pachyderm.y == 1):
            return ("Pachyderm ate.")
        else:
            return ("Pachyderm did not want to eat.")

    def sleep(self):
        if(Pachyderm.y == 1):
            return ("Pachyderm is sleeping.")

        else:
            return ("Pachyderm did not want to sleep.")


    def wakeUp():
        if(Pachyderm.y == 1):
            return ("Pachyderm is awake.")
        else:
            return ("Pachyderm did not want to wake up.")
