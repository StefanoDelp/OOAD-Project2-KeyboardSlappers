import abc
import random
from Pachyderm import *

class Rhino(Pachyderm):
    
    y = random.randint(1,2)
    Names = ""
    food = "Grass"
    def MakeNoise(self):
        print("Rhino Growl")

    def Roam(self):
        if (Rhino.y == 1):
            print ("Rhino roamed.")
        else:
            print ("Rhino did not roam.")

    def Eat(self):
        if(Rhino.y == 1):
            print ("Rhino ate.")
        else:
            print ("Rhino did not want to eat.")

    def Sleep(self):
        if(Rhino.y == 1):
            print ("Rhino is sleeping.")

        else:
            print ("Rhino did not want to sleep.")


    def WakeUp(self):
        if(Rhino.y == 1):
            print ("Rhino is awake.")
        else:
            print ("Rhino did not want to wake up.")
