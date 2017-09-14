from .Animal import Animal

class Bird(Animal):
    beak_length: int = 0

    def __init__(self):
        super().__init__()
        self.read_beak_length()

    def read_beak_length(self):
        self.beak_length = int(input("Enter the length of beak: "))

    def print_animal(self, self_id):
        print("Id = {} | Name - {}, Limbs count - {}, Length of beak - {}"
              .format(self_id, self.nickname, self.limbs_count, self.beak_length))

    def edit(self):
        super().edit()
        self.read_beak_length()
