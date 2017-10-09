from .part2 import *
import pickle

class autopark:
    FILENAME = "st19/file.pkl"
    data = []
    
    def __init__(self):
        pass
        
    def add_car(self):
        car = infcar()
        car.read()
        self.data.append(car)
        print("Информация о машине добавлена")

    def add_fcar(self):
        fcar = fullinfcar()
        fcar.read()
        self.data.append(fcar)
        print("Полная информация о машине добавлена")

    def show_data(self):
        for i in range(0, len(self.data)):
            self.data[i].write()
   
    def wrtf(self):
        pickle_out = open(autopark.FILENAME,"wb")
        pickle.dump(self.data,pickle_out)
        pickle_out.close()
        print("Записано")
        
    def rff(self):
        pickle_in = open(autopark.FILENAME,"rb")
        self.data = pickle.load(pickle_in)
        print("Считано")

    def clear_data(self):
        self.data.clear()
        print("Список чист")

    def edit(self):
        i = input("Введите номер редактируемой машины:")
        print("Введите новые значения:")
        self.data[int(i)].read()
        print("Изменено")

    def dlt(self):
        i = input("Введите номер удаляемой машины:")
        self.data.pop(int(i))
        print("Удалено")
