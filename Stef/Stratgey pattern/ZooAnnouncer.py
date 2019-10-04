from __future__ import annotations
import abc
from abc import ABC, abstractmethod
from random import randrange
from typing import List

"""
    Example taken from https://refactoring.guru/design-patterns/observer/python/example

"""
class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""

"""
Setting all the observer methods to make the annoucment
"""


class ObserverWakeUp(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 1:
            print("Zoo Announcer: The Zoo Keeper is Waking up the Animals")


class ObserverRollCall(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 2:
            print("Zoo Announcer: The Zoo Keeper is Roll Calling the Animals")

class ObserverRoam(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 3:
            print("Zoo Announcer: The Zoo Keeper is Roaming the Animals")


class ObserverEat(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 4:
            print("Zoo Announcer: The Zoo Keeper is Feeding the Animals")


class ObserverSleep(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 5:
            print("Zoo Announcer: The Zoo Keeper is telling the aniamls to go to bed")



 

  
