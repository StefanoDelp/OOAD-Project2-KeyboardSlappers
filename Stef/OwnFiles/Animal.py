import abc
class Animal(abc.ABC):
    @abc.abstractmethod
    def MakeNoise(self):
        pass
    @abc.abstractmethod
    def WakeUp(self):
        pass
    @abc.abstractmethod
    def Response(self):
        pass
    @abc.abstractmethod
    def Roam(self):
        pass
    awake = False
    @abc.abstractmethod
    def Eat(self):
        pass
    @abc.abstractmethod
    def Sleep(self):
        pass