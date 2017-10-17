from .AbstractCommand import AbstractCommand
from ...model.UsedCar import UsedCar


class CommandAddUsedCar(AbstractCommand):
    def invoke(self):
        model = input('Set model name: ')
        year_of_manufacture = int(input('Set year of manufacture: '))
        color = input('Set color: ')
        price = float(input('Set price: '))
        mileage = float(input('Set mileage: '))

        used_car = UsedCar(model, year_of_manufacture, color, price, mileage)
        self._car_showroom.add_car(used_car)

        print('----------')
