from .Bird import Bird, Animal
import pickle


class Zoo:
    __animal_container = []
    ZOO_FILENAME = "st16/zoo.pkl"

    def __init__(self):
        pass

    def add_animal(self):
        animal = Animal()
        self.__animal_container.append(animal)
        print("\nAnimal added!")

    def add_bird(self):
        bird = Bird()
        self.__animal_container.append(bird)
        print("\nBird added!")

    def edit_animal(self):
        if not self.__animal_container:
            print("Zoo is empty!")
            return

        id = int(input("Editable animal id: ")) - 1
        if id < 0:
            raise IndexError
        print("Enter the new values")
        self.__animal_container[id].edit()
        print("\nAnimal edited!")

    def remove_animal(self):
        if not self.__animal_container:
            print("Zoo is empty!")
            return

        id = int(input("Removable animal id: ")) - 1
        if id < 0:
            raise IndexError
        del self.__animal_container[id]
        print("\nAnimal removed!")

    def show_zoo(self):
        if not self.__animal_container:
            print("Zoo is empty!")
            return

        for i in range(0, len(self.__animal_container)):
            self.__animal_container[i].print_animal(i + 1)

    def write_zoo_to_file(self):
        output = open(self.ZOO_FILENAME, 'wb')
        pickle.dump(self.__animal_container, output, -1)
        output.close()
        print("Zoo was writed!")

    def read_zoo_from_file(self):
        pkl_file = open(self.ZOO_FILENAME, 'rb')
        self.__animal_container = pickle.load(pkl_file)
        pkl_file.close()
        print("Zoo was readed!")

    def clear_zoo(self):
        if not self.__animal_container:
            print("Zoo is empty!")
            return

        self.__animal_container.clear()
        print("Zoo is cleared")
