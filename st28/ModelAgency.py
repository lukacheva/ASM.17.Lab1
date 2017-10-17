from .Model import MyClass
from .SuperModel import SecondClass
import pickle

class ModelAgency:
    def __init__(self):
        self.agency=[]

    def insertModel(self):
            newModel = MyClass()
            newModel.read_data()
            self.agency.append(newModel)
            print('Model added!')
            
    def insertSuperModel(self):
            newSuperModel = SecondClass()
            newSuperModel.read_data()
            self.agency.append(newSuperModel)
            print('SuperModel added!')

    def showModelAgency(self):
        for (i,agency) in enumerate (self.agency):
            print('Model number',i+1)
            agency.write_data()

    def edit(self):
        self.showModelAgency()
        print('Enter the number element for edited')
        i=int(input())
        self.agency[i-1].read_data()
        print('Number', i ,'was edited')
            

    def delete(self):
        self.showModelAgency()
        print('Enter the number element for deleted')
        i=int(input())
        self.agency.pop(i-1)
        print('Number', i ,'was deleted')

    def write_file(self):
        f=open('agency.dat','wb')
        pickle.dump(self.agency,f)
        print('Success!')
        
    def read_file(self):
        f=open('agency.dat','rb')
        self.agency = pickle.load(f)
        print('Success!')

    def clean(self):
        self.agency.clear()
        print('Agency is empty!')
        
