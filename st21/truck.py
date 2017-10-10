from st21.modul_show_run import *
from st21.car import car 

class truck(car):

    def __init__(self):
        car.__init__(self)
        self.height=0
        self.carrying=0
        self.edit["height"]=self.add_height
        self.edit["carrying"]=self.add_carrying

    def add(self):
        car.add(self)
        self.add_height()
        self.add_carrying()

    def add_height(self):
        self.height=input("Enter height\n")
        while(True):
            if is_float(self.height):
                break
            else:
                self.height=input("Enter height\n")

    def add_carrying(self):
        self.carrying=input("Enter carrying\n")
        while(True):
            if is_float(self.carrying):
                break
            else:
                self.carrying=input("Enter carrying\n")

    def show_car(self):
        car.show_car(self)
        print("height: "+self.height+"\ncarrying: "+self.carrying)

    def edit_car(self):
        self.show_car()
        while(True):
            inp=input("\nEnter the parameter for editing. To return enter 'back'.\n")
            if (str(inp)=="back"):
                break
            else:
                for i in self.edit:
                    if (str(i)==str(inp)):
                        self.edit[str(inp)]()
