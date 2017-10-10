import datetime

from Run import Run

class Marathon(Run):
    def __init__(self, length=' ', time=' ', date=' ', place=1):
        self.length = length
        self.time = time
        self.date = date
        self.place = place
        
    def create(self):
        self.length = input('Дистанция в км: ')
        self.time = input('Время в мин: ')
        self.place = input('Место: ')
        
        now = datetime.datetime.now()
        self.date = str(now.day) + '.' + str(now.month) + '.' + str(now.year)
        
    def edit(self):
        self.length = input('Дистанция в км (' + self.length + '): ')
        self.time = input('Время в мин (' + self.time + '): ')
        self.place = input('Место (' + self.place + '): ')
        
    def show(self, i):
        hours = int(self.time) // 60
        minutes = int(self.time) - hours * 60
        
        print(str(i) + '. Марафон', self.date + ':', self.length, 'км за', str(hours), 'ч', str(minutes), 'мин.', 'Место:', self.place)
    