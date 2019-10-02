from Animal2 import *
import random
class Canine(Animal):
    Names = ""

    def MakeNoise(self):
        print("Dog")

    y = random.randint(1,2)

    def Roam(self):
        if (Canine.y == 1):
            print ("Canine roamed.")
        else:
            print ("Canine did not roam.")


    def Sleep(self):
        if(Canine.y == 1):
            print ("Canine is sleeping.")

        else:
            print ("Canine did not want to sleep.")


    def WakeUp(self):
        if(Canine.y == 1):
            print ("Canine is awake.")
        else:
            print ("Canine did not want to wake up.")
