from Animal import *
import random
class Canine(Animal):
    Names = ""

    def MakeNoise(self):
        print("Dog")

    #def setName(self):
        #Name = Names
        #return Name
    y = random.randint(1,2)

    def roam(self):
        if (Canine.y == 1):
            return ("Canine roamed.")
        else:
            return ("Canine did not roam.")

    def eat(self):
        if(Canine.y == 1):
            return ("Canine ate.")
        else:
            return ("Canine did not want to eat.")

    def sleep(self):
        if(Canine.y == 1):
            return ("Canine is sleeping.")

        else:
            return ("Canine did not want to sleep.")


    def wakeUp(self):
        if(Canine.y == 1):
            return ("Canine is awake.")
        else:
            return ("Canine did not want to wake up.")
