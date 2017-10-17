from .overseer import *
import pickle


class prison:
    FILENAME = "st22/storage.pkl"
    
    def __init__(self):
        self._stack = []
	
    def _add_person(self, person):
        person.input_data()
        self._stack.append(person)
        print("Person has been added")

    def add_prisoner(self):
        self._add_person(prisoner())
        print("Prisoner has been added")
    
    def add_overseer(self):
        self._add_person(overseer())
	
    
    def print_list(self):
        for i, person in enumerate(self._stack):
            print("ID: ", i)
            person.output_data()
            print()
   
    def clear_list(self):
        self._stack.clear()
        print("All list hase been cleared")
		
		
    def edit_person(self):
        id = input("Enter person ID to edit: ")
        self._stack[int(id)].edit()

    def remove_person(self):
        id = input("Enter person ID to delete: ")
        del self._stack[int(id)]
        print("Person with ID " + id + " has been removed ")

	
	
    def write_to_file(self):
        print("Writing to " + prison.FILENAME)
        with open(prison.FILENAME, "wb") as f:
            pickle.dump(self._stack, f)
        print("Writing has been completed")

    def read_from_file(self):
        print("Reading from " + prison.FILENAME)
        with open(prison.FILENAME, "rb") as f:
            self._stack = pickle.load(f)
        print("Reading has been completed")
