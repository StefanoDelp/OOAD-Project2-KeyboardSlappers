from random import *
from Canine import *
from Feline import *

class Lion(Feline):
    y = random.randint(1,2)
    Names = ""
    food = "Steak"

    def MakeNoise(self):
        print("ROAR")
        
    
    def Roam(self):
        if (Lion.y == 1):
            print ("Lion roamed.")
        else:
            print ("Lion did not roam.")
        
    def Eat(self):
        if(Lion.y == 1):
            print ("Lion ate.")
        else: 
            print ("Lion did not want to eat.")
        
    def Sleep(self):
        if(Lion.y == 1):
            print ("Lion is sleeping.") 
        
        else:
            print ("Lion did not want to sleep.") 
         
     
    def WakeUp(self): 
        if(Lion.y == 1):  
            print ("Lion is awake.") 
        else: 
            print ("Lion did not want to wake up.")