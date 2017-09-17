from .AbstractCommand import AbstractCommand
from ...model.Car import Car


class CommandAddCar(AbstractCommand):
    def invoke(self):
        model = input('Set model name: ')
        year_of_manufacture = int(input('Set year of manufacture: '))
        color = input('Set color: ')
        price = float(input('Set price: '))

        car = Car(model, year_of_manufacture, color, price)
        self._car_showroom.add_car(car)

        print('----------')
