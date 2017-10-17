from abc import ABCMeta, abstractmethod
from ...AbstractCarShowroom import AbstractCarShowroom


class AbstractCommand(metaclass=ABCMeta):
    def __init__(self, car_showroom: AbstractCarShowroom):
        self._car_showroom = car_showroom

    @abstractmethod
    def invoke(self):
        pass
