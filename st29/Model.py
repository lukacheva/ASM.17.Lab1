class MyClass():
    def __init__(self, surname= ' ', name= ' ', age= ' ', growth= ' ', weight= ' '):
        self.surname= surname
        self.name= name
        self.age= age
        self.growth= growth
        self.weight= weight

    def read_data(self):
        self.surname = input("Surname: ", )
        self.name = input("Name: ", )
        self.age = input("Age: ", )
        self.growth = input("Growth: ", )
        self.weight = input("Weight: ", )

    def write_data(self):
        print(self.surname, self.name, self.age, self.growth, self.weight)
        
