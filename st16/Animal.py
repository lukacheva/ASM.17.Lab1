class Animal:
    _nickname: str = None
    _limbs_count: int = None

    def __init__(self):
        self.read_nickname()
        self.read_limbs_count()

    def read_nickname(self):
        self._nickname = input('Enter the nickname: ');

    def read_limbs_count(self):
        self._limbs_count = int(input('Enter the limbs count: '));

    def print_animal(self, self_id):
        print("Id = {} | Name - {}, Limbs count - {}"
              .format(self_id, self._nickname, self._limbs_count))

    def edit(self):
        self.read_nickname()
        self.read_limbs_count()
