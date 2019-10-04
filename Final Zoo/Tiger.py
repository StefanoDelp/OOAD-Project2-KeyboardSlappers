from random import *
from Animal import *
from Feline import *

class Tiger(Feline):

    y = random.randint(1,2)
    Names = ""
    food = "Meat"
    def MakeNoise(self):
        print("ROAR")

    def Roam(self):
        if (Tiger.y == 1):
            print ("Tiger roamed.")
        else:
            print ("Tiger did not roam.")

    def Eat(self):
        if(Tiger.y == 1):
            print ("Tiger ate.")
        else:
            print ("Tiger did not want to eat.")

    def Sleep(self):
        if(Tiger.y == 1):
            print ("Tiger is sleeping.")

        else:
            print ("Tiger did not want to sleep.")


    def WakeUp(self):
        if(Tiger.y == 1):
            print ("Tiger is awake.")
        else:
            print ("Tiger did not want to wake up.")
