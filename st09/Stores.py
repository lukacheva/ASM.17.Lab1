from .Market import Market
from .Department import Department
import pickle


class Stores:

    FILENAME = "st09/dump.pkl"

    def __init__(self):
        self._staff = []

    def _add_dept(self, dept):
        dept.console_input()
        self._staff.append(dept)
        print("Выполнено")

    def add_market(self):
        self._add_dept(Market())

    def add_department(self):
        self._add_dept(Department())

    def print_staff(self):
        for i, dept in enumerate(self._staff):
            print("№ ", i)
            dept.console_output()
            print()

    def clear_staff(self):
        self._staff.clear()
        print("Удалено всё")

    def edit_dept(self):
        id = input("№ отдела изменился: ")
        self._staff[int(id)].edit()

    def remove_dept(self):
        id = input("Удалить отдел № ")
        del self._staff[int(id)]
        print("Отдел с № " + id + " удален ")

    def write_to_file(self):
        Stores.FILENAME = input("Напишите имя файла ")
        with open(Stores.FILENAME, "wb") as f:
            pickle.dump(self._staff, f)
        print("Выполнено")

    def read_from_file(self):
        Stores.FILENAME = input("Напишите имя файла ")
        with open(Stores.FILENAME, "rb") as f:
            self._staff = pickle.load(f)
        print("Выполнено")
