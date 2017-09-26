import pickle

class Guest(object):
    """Базовый класс - гость"""
    def __init__(self):
        self.edit()

    def edit(self):
        print()
        self.name = input("Enter your name, please >> ")
        self.surname = input("Enter your surname, please >> ")
            

    def __str__(self):
        res = "Name: " + self.name +\
              "\nSurname: " + self.surname
        return res
        
##m = Guest()
##s = Registered()
##print(m)
##print(s)
        
