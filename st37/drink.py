from .food import *

class drink(food):
    def __init__(self):
        super().__init__()
        

    def vvod(self):
        self.alcogol = input('Введите алкогольный ли напиток\n')
        super().vvod()
        

    def vyvod(self):
        print('Алкоголь? ' + self.alcogol)
        super().vyvod()
        
