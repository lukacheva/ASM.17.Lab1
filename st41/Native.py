class Native:
    def write(self):
        self.name=input("Укажите исполнителя: ")
        self.albumname=input("Укажите название альбома: ")
        self.populsingle=input("Укажите популярный сингл: ")
        self.year=input("Укажите год выпуска: ")
        self.songs=input("Укажите кол-во песен: ")

    def __str__(self):
        return 'Исполнитель: %s\n название альбома: %s\n популярный сингл: %s\n год выпуска: %s\n кол-во песен: %s\n' %(self.name, self.albumname, self.populsingle, self.year, self.songs)
