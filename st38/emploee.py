from datetime import datetime

class Employee:
    def __init__(self, id):
        self.id = id
        self.set_name()
        self.set_age()
        self.set_start()
        self.set_salary()
        self.editable_attrs = {
            "1": self.set_name,
            "2": self.set_age,
            "3": self.set_start,
            "4": self.set_salary
        }

    def print(self):
        print()
        print("Сотрудник № " + str(self.id))
        print("Имя: " + self.name)
        print("Возраст: " + str(self.age) + " года")
        print("Дата начала работы: " + self.start.strftime("%d/%m/%Y")) 
        print("Зарплата: " + str(self.salary))

    def set_name(self):
        self.name = input("Введите имя сотрудника:\n")

    def set_age(self):
        try:
            self.age = int(input("Введите возраст сотрудника:\n"))
            if self.age < 0:
                raise Exception
        except:
            print("Ошибка! Введите положительное число")
            self.set_age()

    def set_start(self):
        start = input("Введите дату начала работы сотрудника (дд/мм/гггг):\n")
        try:
            self.start = datetime.strptime(start, "%d/%m/%Y")
        except:
            print("Ошибка! Введите данные в указанном формате")
            self.set_start()

    def set_salary(self):
        try:
            self.salary = float(input("Введите зарплату сотрудника\n"))
            if self.salary < 0:
                raise Exception
        except:
            print("Ошибка! Введите положительное число")
            self.set_salary()

    def edit(self):
        self.print_attrs_for_edit()
        action = self.editable_attrs.get(input("\n"))
        if action is not None:
            action()
        else:
            print("Ошибка! Неверный номер атрибута")
            self.edit()

    def print_attrs_for_edit(self):
        print("Какой атрибут вы хотите отредактировать?")
        print("1. Имя")
        print("2. Возраст")
        print("3. Дата начала работы")
        print("4. Зарплата")
        return 4
