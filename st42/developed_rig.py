from .drilling_rig import *

class Developed_rig (Drilling_rig):
    def __init__(self):
        super().__init__()
        self.source_nation = None
        self.colour = None

    def introduction(self):
        super().introduction()
        self.source_nation = input("Введите страну выпуска: ")
        self.colour = input("Введите цвет оборудования: ")

    def result(self):
        super().result()
        print("Страна выпуска: " + self.source_nation)
        print("Цвет оборудования" + self.colour)
        
