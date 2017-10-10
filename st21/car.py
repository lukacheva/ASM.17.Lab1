from st21.modul_show_run import *
class car:

    def __init__(self):
        self.gosnomer=""
        self.mark=""
        self.model=""
        self.horsepower=0
        self.mileage=0
        self.edit={"gosnomer":self.add_gosnomer,
                   "mark":self.add_mark,
                   "model":self.add_model,
                   "horsepower":self.add_horsepower,
                   "mileage":self.add_mileage}

    def add(self):
        self.add_gosnomer()
        self.add_mark()
        self.add_model()
        self.add_horsepower()
        self.add_mileage()

    def add_gosnomer(self):
        self.gosnomer=input("Enter gosnomer\n")

    def add_mark(self):
        self.mark=input("Enter mark\n")

    def add_model(self):
        self.model=input("Enter model\n")
        
    def add_horsepower(self):
        self.horsepower=input("Enter horsepower\n")
        while(True):
            if is_int(self.horsepower):
                break
            else:
                self.horsepower=input("Enter horsepower\n")

    def add_mileage(self):
        self.mileage=input("Enter mileage\n")
        while(True):
            if is_float(self.mileage):
                break
            else:
                self.mileage=input("Enter mileage\n")

    def show_car(self):
        print("\ngosnomer: "+self.gosnomer+"\nmark: "+self.mark+"\nmodel: "+self.model+"\nhorsepower: "+self.horsepower+"\nmileage: "+self.mileage)

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
