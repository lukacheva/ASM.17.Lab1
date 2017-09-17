from .Animal import Animal


class Bird(Animal):
    _beak_length: int = None

    def __init__(self):
        super().__init__()
        self.read_beak_length()

    def read_beak_length(self):
        self._beak_length = int(input("Enter the length of beak: "))

    def print_animal(self, self_id):
        print("Id = {} | Name - {}, Limbs count - {}, Length of beak - {}"
              .format(self_id, self._nickname, self._limbs_count, self._beak_length))

    def edit(self):
        super().edit()
        self.read_beak_length()
