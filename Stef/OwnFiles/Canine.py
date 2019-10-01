from Animal import *
import random
class Canine(Animal):
    Names = ""

    def makeNoise(self):
        print("Dog")
        
    #def setName(self):
        #Name = Names
        #return Name
        
    def Response(self):
        y = random.randint(1,2)
        return y
    
    def roam(self):
        if (Response() == 1):
            return ("Canine roamed.")
        else:
            return ("Canine did not roam.")
        
    def eat(self):
        if(Response() == 1):
            return ("Canine ate.")
        else: 
            return ("Canine did not want to eat.")
        
    def sleep(self):
        if(Response() == 1):
            return ("Canine is sleeping.") 
        
        else:
            return ("Canine did not want to sleep.") 
         
     
    def wakeUp(self): 
        if(Response() == 1):  
            return ("Canine is awake.") 
        else: 
            return ("Canine did not want to wake up.") 