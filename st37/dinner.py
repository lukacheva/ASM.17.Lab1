from .drink import *
import pickle

class dinner:
    kartoteka = []
    f = 'kartoteka.pkl'

    def __init__(self):
        pass

    def add_food(self):
        q = food()
        q.vvod()
        self.kartoteka.append(q)

    def add_drink(self):
        d = drink()
        d.vvod()
        self.kartoteka.append(d)

    def all_(self):
        if len(self.kartoteka)==0:
            print('Элементов нет\n')
        else:
            for i in range(0,len(self.kartoteka)):
                print('\n')
                self.kartoteka[i].vyvod()
          

    def write(self):
        s = open(dinner.f,'wb')
        pickle.dump(self.kartoteka,s)
        s.close()

    def read(self):
        r = open(dinner.f,'rb')
        self.kartoteka = pickle.load(r)
        r.close()

    def edit(self):
        try:
            j = input('Введите номер блюда для изменения\n')
            i = int(j)
            self.kartoteka[i].vvod()
        except IndexError:
            print('Такого элемента в списке нет\n')

    def clear(self):
        self.kartoteka.clear()
        
