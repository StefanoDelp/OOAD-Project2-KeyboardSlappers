import abc
import random
from Animal import *

class Pachyderm(Animal):

    y = random.randint(1,2)

    def MakeNoise(self):
        print("Stomp")

    def Roam(self):
        if (Pachyderm.y == 1):
            print ("Pachyderm roamed.")
        else:
            print ("Pachyderm did not roam.")

    def Eat(self):
        if(Pachyderm.y == 1):
            print ("Pachyderm ate.")
        else:
            print ("Pachyderm did not want to eat.")

    def Sleep(self):
        if(Pachyderm.y == 1):
            print ("Pachyderm is sleeping.")

        else:
            print ("Pachyderm did not want to sleep.")


    def WakeUp(self):
        if(Pachyderm.y == 1):
            print ("Pachyderm is awake.")
        else:
            print ("Pachyderm did not want to wake up.")
