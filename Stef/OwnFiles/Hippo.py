from random import *
from Animal import *
from Pachyderm import *

class Hippo(Pachyderm):

    y = random.randint(1,2)
    Names = ""
    food = "Watermelon"

    def MakeNoise(self):
        print("Snap")
        
    def Roam(self):
        if (Hippo.y == 1):
            print ("Hippo roamed.")
        else:
            print ("Hippo did not roam.")
        
    def Eat(self):
        if(Hippo.y == 1):
            print ("Hippo ate.")
        else: 
            print ("Hippo did not want to eat.")
        
    def Sleep(self):
        if(Hippo.y == 1):
            print ("Hippo is sleeping.") 
        
        else:
            print ("Hippo did not want to sleep.") 
         
     
    def WakeUp(self): 
        if(Hippo.y == 1):  
            print ("Hippo is awake.") 
        else: 
            print ("Hippo did not want to wake up.")