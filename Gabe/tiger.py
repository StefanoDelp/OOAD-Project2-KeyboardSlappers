class Tiger:
    #Class atrributres
    type = 'tiger'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return("{} is {} years old".format(self.name, self.age))

    def speak(self, sound):
        return("{} says {}".format(self.name, sound))
    
thomas = Tiger("Thomas", 10)

print(thomas.description())
print(thomas.speak("RAAWWRRRR XD"))