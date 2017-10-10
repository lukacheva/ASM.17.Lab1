import pickle

from .Run import Run
from .Marathon import Marathon

class RunJournal:
    def __init__(self):
        self.runs = []
        
    def addARun(self):
        newRun = Run()
        newRun.create()
        self.runs.append(newRun)
        print('Пробежка записана.')
        
    def addAMarathon(self):
        newMarathon = Marathon()        
        newMarathon.create()
        self.runs.append(newMarathon)        
        print('Марафон записан.')
        
    def showTheJournal(self):
        print('Записи в журнале:')
        for (i, run) in enumerate(self.runs):
            run.show(i + 1)
    
    def editTheJournal(self):
        self.showTheJournal()
        print('')        
        
        i = int(input('Какую запись отредактировать? '))
        self.runs[i-1].edit()
                
        print('Запись', i, 'отредактирована.')
        
    def deleteARun(self):
        self.showTheJournal()
        print('')
        
        i = int(input('Какую запись стереть? '))
        self.runs.pop(i-1)
        
        print('Запись', i, 'стерта.')
        
    def writeToFile(self):
        f = open('runJournal.dat', 'wb')
        pickle.dump(self.runs, f)
        print('Журнал сохранен в файл.')
        
    def readFromFile(self):
        f = open('runJournal.dat', 'rb')
        self.runs = pickle.load(f)
        print('Журнал из файла прочитан.')
            
    def clearTheJournal(self):
        self.runs.clear()
        print('Теперь журнал пуст.')