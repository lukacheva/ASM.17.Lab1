from .AbstractCommand import AbstractCommand


class CommandDeleteCar(AbstractCommand):
    def invoke(self):
        index = int(input('Enter the item number: '))
        self._car_showroom.delete_car(index - 1)
        print('----------')
