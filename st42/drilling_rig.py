class Drilling_rig:
    def __init__(self):
        self.name = None
        self.date = None
        self.capacity = None

    def introduction(self):
        self.name = input ("Введите модель: ")
        self.date = input("Введите год выпуска: ")
        self.capacity = input("Введите мощность оборудования: ")

    def result(self):
        print ("Модель: " + self.name)
        print ("Год выпуска: " + self.date)    
        print ("Мощность: " + self.capacity + "кВт")
      

         
