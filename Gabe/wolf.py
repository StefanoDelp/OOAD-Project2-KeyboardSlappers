class Wolf:
    #Class atrributres
    type = 'wolf'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return("{} is {} years old".format(self.name, self.age))

    def speak(self, sound):
        return("{} says {}".format(self.name, sound))
    
wolfie = Wolf("Wolfie", 10)

print(wolfie.description())
print(wolfie.speak("Ahhhhh Wooooooooooo"))