from random import *
from Canine import *
from Animal import *

class Lion(Feline):
    y = random.randint(1,2)
    Names = ""
    food = "Steak"

    def makeNoise(self):
        print("ROAR")
        
    ###def setName(Name):
    ###    Names = Name
    ###    return Name
    
    def roam(self):
        if (Lion.y == 1):
            return ("Lion roamed.")
        else:
            return ("Lion did not roam.")
        
    def eat(self):
        if(Lion.y == 1):
            return ("Lion ate.")
        else: 
            return ("Lion did not want to eat.")
        
    def sleep(self):
        if(Lion.y == 1):
            return ("Lion is sleeping.") 
        
        else:
            return ("Lion did not want to sleep.") 
         
     
    def wakeUp(self): 
        if(Lion.y == 1):  
            return ("Lion is awake.") 
        else: 
            return ("Lion did not want to wake up.")