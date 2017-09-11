# Класс студента
class Student:
    first_name: str = ''  # имя
    last_name: str = ''  # фамилия
    age: int = 18  # возраст
    type: str = 'Student'  # заглушка для функции self.info()
    _full_name: str = ''  # private property

    def __init__(self):
        self.set_first_name()
        self.set_last_name()
        self.set_age()
        self._full_name = self.last_name + ' ' + self.first_name

    def info(self) -> str:
        return self.type + ' ' + self.last_name + ' ' + self.first_name + ' ' + str(self.age) + 'y.o.'

    def set_age(self):
        age = input('Set age from ' + self.first_name + '\n')
        try:
            age_int = int(age)
        except ValueError:
            print('Age is number!')
            print(self.first_name + ' is ' + str(self.age) + ' y.o.')
            return
        self.age = age_int

    def get_age(self):
        print(self.age)

    def set_first_name(self):
        self.first_name = input('set first name\n')

    def get_first_name(self):
        print(self.first_name)

    def set_last_name(self):
        self.last_name = input('set last name\n')

    def get_last_name(self):
        print(self.last_name)

    def edit(self):
        self.set_first_name()
        self.set_last_name()
        self.set_age()

    @property
    def full_name(self):
        print(self._full_name)
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        data = full_name.split(' ')
        if len(data) == 2:
            self.last_name = data[0]
            self.first_name = data[1]
            self._full_name = full_name
        else:
            print('Wrong name! Please write format `lastName firstName`')

    @full_name.deleter
    def full_name(self):
        self._full_name = 'No name'
