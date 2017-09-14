class Animal:
    nickname: str = ''
    limbs_count: int = 0

    def __init__(self):
        self.read_nickname()
        self.read_limbs_count()

    def read_nickname(self):
        self.nickname = input('Enter the nickname: ');

    def read_limbs_count(self):
        self.limbs_count = int(input('Enter the limbs count: '));


    def print_animal(self, self_id):
        print("Id = {} | Name - {}, Limbs count - {}"
              .format(self_id, self.nickname, self.limbs_count))

    def edit(self):
        self.read_nickname()
        self.read_limbs_count()
