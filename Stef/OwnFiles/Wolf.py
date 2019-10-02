from Animal import *
from Canine import *

class Wolf(Canine):

    y = random.randint(1,2)
    Names = ""
    food = "Deer"


    def makeNoise(self):
        print("Howl")

    def roam(self):
        if (Wolf.y == 1):
            return ("Wolf roamed.")
        else:
            return ("Wolf did not roam.")

    def eat(self):
        if(Wolf.y == 1):
            return ("Tiger ate.")
        else:
            return ("Wolf did not want to eat.")

    def sleep(self):
        if(Wolf.y == 1):
            return ("Wolf is sleeping.")

        else:
            return ("Wolf did not want to sleep.")


    def wakeUp(self):
        if(Wolf.y == 1):
            return ("Wolf is awake.")
        else:
            return ("Wolf did not want to wake up.")
