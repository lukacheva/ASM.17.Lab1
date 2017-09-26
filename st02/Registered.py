from .Guests import *
#import Guests

class Registered(Guest):
    """Класс потомок - зарегистрированный пользователь"""
    def __init__(self):
        self.edit()

    def edit(self):
        super().edit()
        self.number = int(input("Enter your number, please >> "))

    def __str__(self):
        res = super().__str__() + "\nNumber: " + str(self.number)
        return res
    

