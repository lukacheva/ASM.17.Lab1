from .mage import *
import pickle

class Squad:
    FILENAME = "st05/file.pkl"
    spisok = []
    
    def __init__(self):
        pass
        
    def add_warrior(self):
        warrior = Warrior()
        warrior.read_c()
        self.spisok.append(warrior)
        print("Воин добавлен")

    def add_mage(self):
        mage = Mage()
        mage.read_c()
        self.spisok.append(mage)
        print("Воин-маг добавлен")

    def show_spisok(self):
        for i in range(0, len(self.spisok)):
            self.spisok[i].write_c()
   
    def wrtf(self):
        pickle_out = open(Squad.FILENAME,"wb")
        pickle.dump(self.spisok,pickle_out)
        pickle_out.close()
        print("Записано")
        
    def rff(self):
        pickle_in = open(Squad.FILENAME,"rb")
        self.spisok = pickle.load(pickle_in)
        print("Считано")

    def clear_spisok(self):
        self.spisok.clear()
        print("Список чист")

    def edit(self):
        i = input("Введите номер редактируемого воина:")
        print("Введите новые значения:")
        self.spisok[int(i)].read_c()
        print("Изменено")

    def dlt(self):
        i = input("Введите номер удаляемого воина:")
        self.spisok.pop(int(i))
        print("Удалено")
