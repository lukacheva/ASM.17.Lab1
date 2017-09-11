from .Employee import Employee
from .Supervisor import Supervisor
import pickle


class Company:

    FILENAME = "st39/dump.pkl"

    def __init__(self):
        self._staff = []

    def _add_person(self, person):
        person.console_input()
        self._staff.append(person)
        print("Done")

    def add_employee(self):
        self._add_person(Employee())

    def add_supervisor(self):
        self._add_person(Supervisor())

    def print_staff(self):
        for i, person in enumerate(self._staff):
            print("ID: ", i)
            person.console_output()
            print()

    def clear_staff(self):
        self._staff.clear()
        print("Staff list cleared")

    def edit_person(self):
        id = input("Person ID to edit: ")
        self._staff[int(id)].edit()

    def remove_person(self):
        id = input("Person ID to delete: ")
        del self._staff[int(id)]
        print("Person with ID# " + id + " removed ")

    def write_to_file(self):
        print("Writing to " + Company.FILENAME)
        with open(Company.FILENAME, "wb") as f:
            pickle.dump(self._staff, f)
        print("Done")

    def read_from_file(self):
        print("Reading from " + Company.FILENAME)
        with open(Company.FILENAME, "rb") as f:
            self._staff = pickle.load(f)
        print("Done")