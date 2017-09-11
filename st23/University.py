import pickle

from st23.Teacher import Student, Teacher


# Класс-контейнер университета
class University:
    name: str = ''  # название университета
    people = []  # список людей

    def __init__(self, name: str = 'RGUNG'):
        self.name = name

    def set_name(self):
        self.name = input('Set university\'s name \n')

    def get_name(self):
        print(self.name)

    def add_student(self):
        man: Student = Student()
        self.add_man(man)

    def add_teacher(self):
        man: Teacher = Teacher()
        self.add_man(man)

    def add_man(self, man):
        print('Hello, ' + man.first_name)
        self.people.append(man)

    def remove_man(self):
        self.show_people()
        if len(self.people) == 0:
            return
        index = input('set index\n')
        if -1 < int(index) < len(self.people):
            self.people.pop(int(index))
            print(self.name + ' lost 1 man :(')
        else:
            print('Incorrect index')

    def clear_men(self):
        print('All people was killed! :)')
        self.people = []

    def show_people(self):
        if len(self.people) == 0:
            print('University ' + self.name + ' is empty')
            return
        print('University ' + self.name + ' has:')
        for index, man in enumerate(self.people):
            print(str(index) + '. ' + man.info())

    def save_list(self):
        with open('st23/storage', 'wb') as f:
            pickle.dump(self.people, f)
        print('Done!')

    def get_list(self):
        with open('st23/storage', 'rb') as f:
            mans = pickle.load(f)
            self.clear_men()
            for man in mans:
                if type(man) is Student or type(man) is Teacher:
                    self.people.append(man)
            self.show_people()

    def edit(self):
        self.set_name()

    def edit_mans(self):
        self.show_people()
        if len(self.people) == 0:
            return
        index = input('set man\'s index\n')
        try:
            man = self.people[int(index)]
            man.edit()
        except ValueError:
            print('Index is number')
        except IndexError:
            print('Index out of range')
