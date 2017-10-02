from .developed_rig import *
import pickle

class Place:
    Urengoy = "st42/file.pkl"
    atribut = []

    def __init__(self):
        pass

    def add_rig(self):
        rig = Drilling_rig()
        rig.introduction()
        self.atribut.append(rig)
        print ("Установка добалена")

    def add_modified_rig(self):
        modified_rig = Developed_rig()
        modified_rig.introduction()
        self.atribut.append(modified_rig)
        print ("Модифицированная установка добавлена")

    def display_atribut(self):
        for a in self.atribut:
            a.result()

    def read(self):
        understand = open(Place.Urengoy,"rb")
        self.atribut = pickle.load(understand)
        print ("Прочитано")

    def write(self):
        letter = open(Place.Urengoy,"wb")
        pickle.dump(self.atribut,letter)
        letter.close()
        print("Засчитано")

    def clean_out(self):
        self.atribut.clear()
        print ("Очищено")

    def edit(self):
        b = input("Запишите номер оборудования, который вы изволите редактировать: ")
        print("Запишите обновлённое оборудование")
        self.atribut[int(b)].introduction()
        print("Редактировано")

    def delete(self):
        b = input("Запишите номер оборудования, который вы хотите устранить: ")
        self.atribut.pop(int(b))
        print("Устранено")
        
