import pickle
from .used import *

class Catalog:
    def __init__(self):
        self.catalog = []

    def add_new(self):
        auto = Auto()
        self.catalog.append(auto)
        print ('Новый автомобиль добавлен')
        return

    def add_used(self):
        auto = Used()
        self.catalog.append(auto)
        print ('Подержанный автомобиль добавлен')
        return 
    
    def show_catalog(self):
        if len(self.catalog)==0:
            print('Каталог пуст')
        else:
            print('Каталог:: ')
            i=1
            for item in self.catalog:
                print ("{0}) {1} ".format (i, item.name))
                i+=1
            return 0
    
    def edit_catalog(self):
        if len(self.catalog)==0:
            print('Каталог пуст')
        else:
            print('Выберите автомобиль')
            i = 1
            for item in self.catalog:
                print("{0}) {1}".format(i, item.name))
                i+=1
            try:
                i = int(input('Введите номер: '))
                self.catalog[i-1].__init__()
                print('Редактирование завершено')
            except:
                print('Неверный ввод\n')
                self.edit_catalog()
            return
        
    def delete_auto(self):
        if len(self.catalog)==0:
            print('Каталог пуст')
        else:
            print('Выберите автомобиль')
            i = 1
            for item in self.catalog:
                print("{0}) {1}".format(i, item.name))
                i+=1
            try:
                i = int(input('Введите номер: '))
                self.catalog.pop(i-1)
                print('Автомобиль удален\n')
            except:
                print('Неверный ввод\n')
                self.delete_auto()
            return

    def clear_catalog(self):
        self.catalog.clear()
        print('Каталог очищен')
        return

    def save_catalog(self):
        pickle.dump(self.catalog, open('st24/cata.log', 'wb'))
        print('Каталог сохранен')
        return

    def load_catalog(self):
        self.catalog = pickle.load(open('st24/cata.log', 'rb'))
        print('Каталог загружен')
        return 
