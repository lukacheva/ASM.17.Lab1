class Auto:
    def __init__(self):
        self.name = input('Название: ')
        self.year = input('Год выпуска: ')
        self.color = input ('Цвет: ')

    def __str__(self):
        out = ('Название: ' + self.name
               + '\nГод выпуска: ' + self.year
               + '\nЦвет: ' + self.color)
        return out
