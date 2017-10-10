import pickle 
from .Native import *
from .Foreign import *

class Music:
    def __init__(self):
        self.albums=[]
        
    def AddNative(self):
        album=Native()
        album.write()
        self.albums.append(album)

    def AddForeign(self):
        album=Foreign()
        album.write()
        self.albums.append(album)
        
    def ShowList(self):
        if len(self.albums)==0:
            print("Список пуст!")
        else:
            i = 0
            print("Список:")
            for x in self.albums:
                print(i,x)
                i+=1
            
    def ClearList(self):
        self.albums.clear()
        print("Список очищен!")

    def WriteToFile(self):
        pickle.dump(self.albums, open('file.dat', 'wb'))
        print("Запись в файл успешно выполнена!")

    def ReadFromFile(self):
        self.albums=pickle.load(open('file.dat', 'rb'))
        print("Чтение из файла успешно выполнено!")

    def ChangeAlbum(self):
        if len(self.albums)==0:
            print("список пуст!")
            return
        n=int(input("Введите номер объекта:"))
        if n<=len(self.albums)-1 and 0<=n:
            print("Успешный ввод!")
            self.albums[n].write()
            print("Замена успешно выполнена!")
        else:
            print("Ошибка ввода!")
            
    def DeleteAlbum(self):
        if len(self.albums)==0:
            print("список пуст! ")
            return
        n=int(input("Введите номер объекта: "))
        if n<=(self.index-1) and 0<=n:
            print("Успешный ввод!")
            self.albums.pop(n)
            print("удаление успешно выполнено! ") 
        else:
            print ("Ошибка ввода!")
