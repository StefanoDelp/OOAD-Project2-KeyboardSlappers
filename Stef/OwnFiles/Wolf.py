from Animal import *
from Canine import *

class Wolf(Canine):
    def Response(self):
        y = random.randint(1,2)
        return y
    Names = ""
    food = "Deer"
    resp  = Response(self)
    def makeNoise(self):
        print("Howl")
          
    def setName(self):
        Names = Name
        return Name
    
    def roam(self):
        if (Response() == 1):
            return ("Wolf roamed.")
        else:
            return ("Wolf did not roam.")
        
    def eat(self):
        if(Response() == 1):
            return ("Tiger ate.")
        else: 
            return ("Wolf did not want to eat.")
        
    def sleep(self):
        if(Response() == 1):
            return ("Wolf is sleeping.") 
        
        else:
            return ("Wolf did not want to sleep.") 
         
     
    def wakeUp(self): 
        if(Response() == 1):  
            return ("Wolf is awake.") 
        else: 
            return ("Wolf did not want to wake up.")
        