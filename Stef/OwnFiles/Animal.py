import abc
class Animal(abc.ABC):
    @abc.abstractmethod
    def makeNoise(self):
        pass
    @abc.abstractmethod
    def setName(self):
        pass
    @abc.abstractmethod
    def wakeUp(self):
        pass
    @abc.abstractmethod
    def Response(self):
        pass
    @abc.abstractmethod
    def roam(self):
        pass
    awake = False
    @abc.abstractmethod
    def eat(self):
        pass
    @abc.abstractmethod
    def sleep(self):
        pass