from .Native import *
class Foreign(Native):
    def write(self):
        super().write()
        self.country=input("Укажите страну: ")

    def __str__(self):
        return 'Исполнитель: %s\n альбом: %s\n популярный сингл: %s\n год выпуска: %s\n кол-во песен: %s\n страна: %s\n' %(self.name, self.albumname, self.populsingle, self.year, self.songs, self.country)
