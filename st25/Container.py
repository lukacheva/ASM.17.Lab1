from .Goalkeeper import Goalkeeper, Player
import pickle

class Container:
    player_container = []
    CONTAINER_FILE = "st26/container.pkl"

    def __init__(self):
        pass

    def add_player(self):
        player = Player()
        self.player_container.append(player)
        print("\nPlayer added!")

    def add_goalkeeper(self):
        goalkeeper = Goalkeeper()
        self.player_container.append(goalkeeper)

    def edit_player(self):
        if not self.player_container:
            print ("Container is empty")
            return

        id = int(input("Editable player id: ")) - 1
        print("Enter the new values")
        self.player_container[id].edit()
        print("\nPlayer edited!")

    def remove_player(self):
        if not self.player_container:
            print("Container is empty!")
            return

        id = int(input("Removable player id: ")) - 1

        del self.player_container[id]
        print("\nPlayer removed!")

    def show_container(self):
        if not self.player_container:
            print("Container is empty!")
            return

        for i in range(0, len(self.player_container)):
            self.player_container[i].print_player(i + 1)

    def write_container_to_file(self):
        output = open(self.CONTAINER_FILE, 'wb')
        pickle.dump(self.player_container, output, -1)
        output.close()
        print("Conteainer was writed!")

    def read_container_from_file(self):
        pkl_file = open(self.CONTAINER_FILE, 'rb')
        self.player_container = pickle.load(pkl_file)
        pkl_file.close()
        print("Container was readed!")

    def clear_container(self):
        if not self.player_container:
            print("Container is empty!")
            return

        self.player_container.clear()
        print("Container is cleared")