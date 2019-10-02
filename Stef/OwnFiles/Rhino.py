import abc
import random

class Rhino(Pachyderm):
    def Response():
        y = random.randint(1,2)
        return y
    Names = ""
    food = "Grass";
    resp  = Response();
    def makeNoise(self):
        print("Rhino Growl")

    def setName(Name):
        Names = Name
        return Name

    def roam():
        if (Response() == 1):
            return ("Rhino roamed.")
        else:
            return ("Rhino did not roam.")

    def eat():
        if(Response() == 1):
            return ("Rhino ate.")
        else:
            return ("Rhino did not want to eat.")

    def sleep():
        if(Response() == 1):
            return ("Rhino is sleeping.")

        else:
            return ("Rhino did not want to sleep.")


    def wakeUp():
        if(Response() == 1):
            return ("Rhino is awake.")
        else:
            return ("Rhino did not want to wake up.")
