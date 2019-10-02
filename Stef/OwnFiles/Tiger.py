from random import *
from Animal import *
from Feline import *

class Tiger(Feline):

    y = random.randint(1,2)
    Names = ""
    food = "Meat"
    def MakeNoise(self):
        print("ROAR")

    ###def setName(Name):
    ###    Names = Name
    ###    return Name

    def Roam(self):
        if (Tiger.y == 1):
            return ("Tiger roamed.")
        else:
            return ("Tiger did not roam.")

    def Eat(self):
        if(Tiger.y == 1):
            return ("Tiger ate.")
        else:
            return ("Tiger did not want to eat.")

    def Sleep(self):
        if(Tiger.y == 1):
            return ("Tiger is sleeping.")

        else:
            return ("Tiger did not want to sleep.")


    def wakeUp(self):
        if(Tiger.y == 1):
            return ("Tiger is awake.")
        else:
            return ("Tiger did not want to sleep.")


    def WakeUp(self):
        if(Tiger.y == 1):
            return ("Tiger is awake.")
        else:
            return ("Tiger did not want to wake up.")
