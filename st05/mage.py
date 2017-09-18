from .warrior import *

class Mage(Warrior):
    def __init__(self):
        super().__init__()
        self.mana = None
        self.spell = None
 
    def read_c(self):
        super().read_c()
        self.mana = input("Введите ману:")
        self.spell = input("Введите заклинание:")

    def write_c(self):
        super().write_c()
        print("Мана: " + self.mana)
        print("Заклинание: " + self.spell)
