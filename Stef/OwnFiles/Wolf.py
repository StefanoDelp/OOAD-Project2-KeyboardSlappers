from Animal import *
from Canine import *
import random

class Wolf(Canine):

    y = random.randint(1,2)
    Names = ""
    food = "Deer"


    def MakeNoise(self):
        print("Howl")

    def Roam(self):
        if (Wolf.y == 1):
            return ("Wolf roamed.")
        else:
            return ("Wolf did not roam.")

    def Eat(self):
        if(Wolf.y == 1):
            return ("Tiger ate.")
        else:
            return ("Wolf did not want to eat.")

    def Sleep(self):
        if(Wolf.y == 1):
            return ("Wolf is sleeping.")

        else:
            return ("Wolf did not want to sleep.")


    def wakeUp(self):
        if(Wolf.y == 1):
            return ("Wolf is awake.")
        else:
            return ("Wolf did not want to sleep.")


    def WakeUp(self):
        if(Wolf.y == 1):
            return ("Wolf is awake.")
        else:
            return ("Wolf did not want to wake up.")
