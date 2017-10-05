from st17.ListCommand import *

class Dish:

    def __init__(self):
        self.name=""
        self.price=0
        self.grams=0
        self.description=""
        self.edit=[self.AddName,self.AddPrice,self.AddGrams,self.AddDescription]
    
    def AddDish(self):
        self.AddName()
        self.AddPrice()
        self.AddGrams()
        self.AddDescription()

    def AddName(self):
        self.name=input("Enter name\n")
    
    def AddPrice(self):
        self.price=input("Enter price\n")
        while(True):
            if IsFloat(self.price):
                break
            else:
                self.price=input("Enter price\n")

    def AddGrams(self):
        self.grams=input("Enter grams\n")
        while(True):
            if IsFloat(self.grams):
                break
            else:
                self.grams=input("Enter price\n")

    def AddDescription(self):
        self.description=input("Enter description\n")

    def ShowDish(self):
        print("\n0) name - "+self.name+"\n1) price - "+self.price+"\n2) grams - "+self.grams+"\n3) description - "+self.description)

    def EditDish(self):
        self.ShowDish()
        i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
        while(True):
            if IsInt(i):
                break
            else:
                i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
        while(int(i)!=-1):
            self.edit[int(i)]()
            self.ShowDish()
            i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
            while(True):
                if IsInt(i):
                    break
                else:
                    i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
