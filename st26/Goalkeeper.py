from .Player import Player

class Goalkeeper(Player):

    def __init__(self):
        super().__init__()
        self.read_reaction()

    def read_reaction(self):
        self.reaction = int(input("Enter the reaction: "))

    def print_player(self, self_id):
        print("Id = {} | Name - {}, Raiting - {}, Reaction - {}"
              .format(self_id, self.playername, self.raiting, self.reaction))

    def edit(self):
        super().edit()
        self.read_reaction()