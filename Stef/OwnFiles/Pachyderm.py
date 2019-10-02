import abc
import random
from Animal import *

class Pachyderm(Animal):
    def Response():
        y = random.randint(1,2)
        return y
    resp  = Response();
    def makeNoise(self):
        print("Stomp")

    def setName(Name):
        Names = Name
        return Name

    def roam():
        if (Response() == 1):
            return ("Pachyderm roamed.")
        else:
            return ("Pachyderm did not roam.")

    def eat():
        if(Response() == 1):
            return ("Pachyderm ate.")
        else:
            return ("Pachyderm did not want to eat.")

    def sleep():
        if(Response() == 1):
            return ("Pachyderm is sleeping.")

        else:
            return ("Pachyderm did not want to sleep.")


    def wakeUp():
        if(Response() == 1):
            return ("Pachyderm is awake.")
        else:
            return ("Pachyderm did not want to wake up.")
