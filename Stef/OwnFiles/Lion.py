from random import *
from Canine import *
from Feline import *

class Lion(Feline):
    y = random.randint(1,2)
    Names = ""
    food = "Steak"

    def MakeNoise(self):
        print("ROAR")
        
    ###def setName(Name):
    ###    Names = Name
    ###    return Name
    
    def Roam(self):
        if (Lion.y == 1):
            return ("Lion roamed.")
        else:
            return ("Lion did not roam.")
        
    def Eat(self):
        if(Lion.y == 1):
            return ("Lion ate.")
        else: 
            return ("Lion did not want to eat.")
        
    def Sleep(self):
        if(Lion.y == 1):
            return ("Lion is sleeping.") 
        
        else:
            return ("Lion did not want to sleep.") 
         
     
    def WakeUp(self): 
        if(Lion.y == 1):  
            return ("Lion is awake.") 
        else: 
            return ("Lion did not want to wake up.")