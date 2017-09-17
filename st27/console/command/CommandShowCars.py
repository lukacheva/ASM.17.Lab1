from .AbstractCommand import AbstractCommand
from ...model.AbstractCar import AbstractCar


class CommandShowCars(AbstractCommand):
    def print_car(self, car: AbstractCar):
        data = car.get_data()
        for key in data:
            print(key + ': ' + str(data[key]))

    def invoke(self):
        if self._car_showroom.is_empty():
            print('car showroom is empty')
            print('----------')
            return

        cars = self._car_showroom.get_all()
        number = 1
        for car in cars:
            if not isinstance(car, AbstractCar):
                raise RuntimeError('Unknown instance')
            print(str(number) + '.')
            self.print_car(car)
            print('----------')
            number += 1
