from .auto import *

class Used(Auto):
    def __init__(self):
        super().__init__()
        self.owners = input('Кол-во владельцев: ')
        self.mileage = input ('Пробег: ')
    def __str__(self):
        super().__str__()
        out = ('\nКол-во владельцев: ' + self.owners
           + '\nПробег: ' + self.mileage)
        return out
