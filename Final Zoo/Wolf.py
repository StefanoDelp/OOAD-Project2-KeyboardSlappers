from Animal2 import *
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
            print ("Wolf roamed.")
        else:
            print ("Wolf did not roam.")



    def Sleep(self):
        if(Wolf.y == 1):
            print ("Wolf is sleeping.")

        else:
            print ("Wolf did not want to sleep.")

    def WakeUp(self):
        if(Wolf.y == 1):
            print ("Wolf is awake.")
        else:
            print ("Wolf did not want to wake up.")
