from .student import *

class Mayor(Student):
    def __init__(self):
        super().__init__()
        self.telephone = ""
    
    def read(self):
        super().read()
        self.telephone = input("Введите номер телефона: ")

    def write(self):
        super().write()
        print("Номер телефона: ", self.telephone)
