from .AbstractCommand import AbstractCommand
from ...model.Car import Car
from ...model.UsedCar import UsedCar


class CommandEditCar(AbstractCommand):
    def invoke(self):
        if self._car_showroom.is_empty():
            print('car showroom is empty')
            print('----------')
            return

        index = int(input('Enter the item number: '))
        car = self._car_showroom.get(index - 1)

        if not isinstance(car, Car) and not isinstance(car, UsedCar):
            raise RuntimeError('Unknown instance')

        if isinstance(car, Car):
            model = input('Set model name (' + str(car.get_model()) + '): ')
            if model:
                car.set_model(model)

            year_of_manufacture = input('Set year of manufacture (' + str(car.get_year_of_manufacture()) + '): ')
            if year_of_manufacture:
                car.set_year_of_manufacture(int(year_of_manufacture))

            color = input('Set color (' + str(car.get_color()) + '): ')
            if color:
                car.set_color(color)

            price = input('Set price (' + str(car.get_price()) + '): ')
            if price:
                car.set_price(float(price))

        if isinstance(car, UsedCar):
            mileage = input('Set mileage (' + str(car.get_mileage()) + '): ')
            if mileage:
                car.set_mileage(float(mileage))

        print('----------')
