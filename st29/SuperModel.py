from Model import MyClass

class SecondClass(MyClass):
    def __init__(self, surname = ' ', name= ' ', age= ' ', growth= ' ', weight= ' ',magazine= ' '):
        self.magazine = magazine;
        MyClass.__init__(self, surname, name, age, growth, weight)
    
    def read_data(self):
        MyClass.read_data(self)
        self.magazine = input("Magazine: ", )

    def write_data(self):
        print(self.surname, self.name, self.age, self.growth, self.weight,self.magazine)
    
        
