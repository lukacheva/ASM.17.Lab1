from .Employee import Employee


class Supervisor(Employee):
    def __init__(self):
        super().__init__()
        self._responsibility = None
        self._liberties = None

    def console_input(self):
        super().console_input()
        self._responsibility = input("Responsibility: ")
        self._liberties = input("Liberties: ")

    def console_output(self):
        super().console_output()
        print("Responsibility: " + self._responsibility)
        print("Liberties: " + self._liberties)

    def edit(self):
        super().edit()
        self._responsibility = input("New responsibility: ")
        self._liberties = input("New liberties ")
