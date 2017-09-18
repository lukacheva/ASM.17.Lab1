class Warrior:
    def __init__(self):
        self.name = None
        self.health = None
        self.attack = None
        
    def read_c(self):
        self.name = input("Введите имя:")
        self.health = input("Введите здоровье:")
        self.attack = input("Введите силу атаки:")

    def write_c(self):
        print("Имя: " + self.name)
        print("Здоровье: " + self.health)
        print("Сила атаки: " + self.attack)
