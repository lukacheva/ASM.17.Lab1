class Actor:
    def __init__(self):
        self.enter_name()
        self.enter_age()
        self.enter_role()

        self.editing_attributes = [
            self.enter_name,
            self.enter_age,
            self.enter_role
        ]

        self.edit_message = [
            '[0] -  name\n',
            '[1] - age\n',
            '[2] - role\n'
        ]

        self.printing_bio = [self.print_name, self.print_age, self.print_role]

    def print_bio(self):
        for print_info in self.printing_bio:
            print_info()

    def print_role(self):
        print('%s\'s role is "%s"' % (self.name, self.role))

    def print_name(self):
        print('This is %s' % self.name)

    def print_age(self):
        print('%s is %s years now' % (self.name, self.age))

    def enter_name(self):
        self.name = input('Input new name: ')

    def enter_age(self):
        self.age = input('Input new age: ')

    def enter_role(self):
        self.role = input('Input new role: ')

    def edit_bio(self):
        action_digit = input(
            'What info do you want to change: \n%s'
            'Input one digit: ' % ''.join(self.edit_message)
        )

        try:
            self.editing_attributes[int(action_digit)]()
        except:
            print('Wrong input data')


if __name__ == '__main__':
    pass
