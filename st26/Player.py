class Player:

    def __init__(self):
        self.read_playername()
        self.read_raiting()

    def read_playername(self):
        self.playername = input('Enter the player name: ');

    def read_raiting(self):
        self.raiting = int(input('Enter the raiting: '));

    def print_player(self, self_id):
        print("Id = {} , Name - {}, Raiting - {}"
              .format(self_id, self.playername, self.raiting))

    def edit(self):
        self.read_playername()
        self.read_raiting()