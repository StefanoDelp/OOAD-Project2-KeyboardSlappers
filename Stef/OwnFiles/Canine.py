from Animal import *
import random
class Canine(Animal):
    Names = ""

    def MakeNoise(self):
        print("Dog")
        
    #def setName(self):
        #Name = Names
        #return Name
        
    def Response(self):
        y = random.randint(1,2)
        return y
    
    def Roam(self):
        if (Response() == 1):
            return ("Canine roamed.")
        else:
            return ("Canine did not roam.")
        
    def Eat(self):
        if(Response() == 1):
            return ("Canine ate.")
        else: 
            return ("Canine did not want to eat.")
        
    def Sleep(self):
        if(Response() == 1):
            return ("Canine is sleeping.") 
        
        else:
            return ("Canine did not want to sleep.") 
         
     
    def WakeUp(self): 
        if(Response() == 1):  
            return ("Canine is awake.") 
        else: 
            return ("Canine did not want to wake up.") 