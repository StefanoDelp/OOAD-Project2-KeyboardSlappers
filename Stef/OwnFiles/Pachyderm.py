import abc
import random
from Animal import *

class Pachyderm(Animal):

    y = random.randint(1,2)

    def MakeNoise(self):
        print("Stomp")

    def Roam(self):
        if (Pachyderm.y == 1):
            return ("Pachyderm roamed.")
        else:
            return ("Pachyderm did not roam.")

    def Eat(self):
        if(Pachyderm.y == 1):
            return ("Pachyderm ate.")
        else:
            return ("Pachyderm did not want to eat.")

    def Sleep(self):
        if(Pachyderm.y == 1):
            return ("Pachyderm is sleeping.")

        else:
            return ("Pachyderm did not want to sleep.")


    def WakeUp(self):
        if(Pachyderm.y == 1):
            return ("Pachyderm is awake.")
        else:
            return ("Pachyderm did not want to wake up.")
