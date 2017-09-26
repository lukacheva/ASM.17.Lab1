from .Guests import *
from .Registered import *
import pickle

class Library:
    """Класс контейнер - библиотека"""
    def __init__(self):
        self.l = list()

    def add_Guest(self):
        self.add(Guest())

    def add_Regustered(self):
        self.add(Registered())

    def add(self, student):
        self.l.append(student)

    def print_list(self):
        if self.l:
            for i, o in enumerate(self.l):
                print('№', i)
                print(o)
        else:
            print("Список пуст")

    def in_file(self):
        if self.l:
            with open('file.bat', 'wb') as f:
                pickle.dump(self.l, f)
            print("success")
        else:
            print("Список пуст")

    def out_file(self):
        if self.l:
            with open('file.bat', 'rb') as f:
                self.l = pickle.load(f)
            print("success")
        else:
            print("Список пуст")

    def clear_list(self):
        self.l = []
        print("list clear")

    def del_student(self):
        index = int(input("Enter the index number >> "))
        del self.l[index]

    def edit_student(self):
        index = int(input("Enter the index number >> "))
        self.l[index].edit()
        
        
        
