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
            return ("Hippo roamed.")
        else:
            return ("Hippo did not roam.")
        
    def Eat(self):
        if(Hippo.y == 1):
            return ("Hippo ate.")
        else: 
            return ("Hippo did not want to eat.")
        
    def Sleep(self):
        if(Hippo.y == 1):
            return ("Hippo is sleeping.") 
        
        else:
            return ("Hippo did not want to sleep.") 
         
     
    def WakeUp(self): 
        if(Hippo.y == 1):  
            return ("Hippo is awake.") 
        else: 
            return ("Hippo did not want to wake up.")