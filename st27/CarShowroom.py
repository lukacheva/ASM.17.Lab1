from .AbstractCarShowroom import AbstractCarShowroom
from .model.AbstractCar import AbstractCar


class CarShowroom(AbstractCarShowroom):
    __cars: []

    def __init__(self, cars: [] = None):
        if cars is None:
            self.__cars = []
        else:
            self.__cars = cars

    def set_cars(self, cars: [AbstractCar]):
        self.__cars = cars

    def add_car(self, car: AbstractCar):
        self.__cars.append(car)
        return self

    def delete_car(self, index: int):
        self.__cars.pop(index)
        return self

    def get(self, index: int) -> AbstractCar:
        return self.__cars[index]

    def get_all(self) -> [AbstractCar]:
        return self.__cars

    def clear(self):
        self.__cars.clear()
        return self

    def is_empty(self) -> bool:
        return len(self.__cars) == 0
