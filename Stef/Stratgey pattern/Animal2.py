import abc
from abc import ABC, abstractmethod
from typing import List

class Strategy(abc.ABC):

    @abstractmethod
    def Eat(self):
        pass


class Animal(abc.ABC):
    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy
    @abc.abstractmethod
    def MakeNoise(self):
        pass
    @abc.abstractmethod
    def WakeUp(self):
        pass
    @abc.abstractmethod
    def Roam(self):
        pass
    awake = False
    @abc.abstractmethod
    def Sleep(self):
        pass

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def Eat(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        result = self._strategy.Eat()
        print(result)

        # ...


class FeedWithCare(Strategy):
    def Eat(self):
        return("Animal Fed with Care")

class FeedWithFear(Strategy):
    def Eat(self):
        return("Wolf Fed with Fear")
