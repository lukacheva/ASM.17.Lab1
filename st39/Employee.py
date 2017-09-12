class Employee:
    def __init__(self):
        self._name = None
        self._position = None
        self._salary = None

    def console_input(self):
        self._name = input("Name: ")
        self._position = input("Position: ")
        self._salary = input("Salary: ")

    def console_output(self):
        print("Name: " + self._name)
        print("Position: " + self._position)
        print("Salary: " + self._salary)

    def edit(self):
        self._name = input("New name: ")
        self._position = input("New position: ")
        self._salary = input("New salary: ")