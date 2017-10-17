from .part1 import *
class fullinfcar(infcar):

    def __init__(self):
        super().__init__()
        self.power = None
        self.speed = None

    def read(self):
        super().read()
        self.power = input("Введите мощность:")
        self.speed = input("Введите скорость:")

    def write(self):
        super().write()
        print("Мощность: " + self.power)
        print("Скорость: " + self.speed)
