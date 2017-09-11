from st23.Student import Student


# Класс учителя, который вырос из студента
class Teacher(Student):
    degree: str = ''  # звание преподавателя
    workplace: str = ''  # место работы
    salary: int = 1000  # размер зарплаты

    def __init__(self):
        Student.__init__(self)
        self.type = 'Teacher'
        self.set_degree()
        self.set_salary()

    # Переопределяем функцию
    def info(self) -> str:
        return self.degree + ' ' + Student.info(self)

    def set_degree(self):
        self.degree = input('Set degree\n')

    def get_degree(self):
        print(self.degree)

    # Переопределяем функцию
    def edit(self):
        Student.edit(self)
        self.set_degree()
        self.set_salary()

    def set_workplace(self):
        self.workplace = input('Set workplace\n')

    def get_workplace(self):
        print(self.workplace)

    def set_salary(self):
        salary = input('Set salary\n')
        try:
            salary_int = int(salary)
        except ValueError:
            print('Salary is number!')
            print('Standart salary is ' + str(self.salary))
            return
        self.salary = salary_int
