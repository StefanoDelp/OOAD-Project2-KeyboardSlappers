from random import *
from Animal import *
from Pachyderm import *

class Hippo(Pachyderm):

    y = random.randint(1,2)
    Names = ""
    food = "Watermelon"

    def makeNoise(self):
        print("Snap")
        
    ###def setName(Name):
    ###    Names = Name
    ###    return Name
    
    def roam(self):
        if (Hippo.y == 1):
            return ("Hippo roamed.")
        else:
            return ("Hippo did not roam.")
        
    def eat(self):
        if(Hippo.y == 1):
            return ("Hippo ate.")
        else: 
            return ("Hippo did not want to eat.")
        
    def sleep(self):
        if(Hippo.y == 1):
            return ("Hippo is sleeping.") 
        
        else:
            return ("Hippo did not want to sleep.") 
         
     
    def wakeUp(self): 
        if(Hippo.y == 1):  
            return ("Hippo is awake.") 
        else: 
            return ("Hippo did not want to wake up.")