from .emploee import Employee

class Developer(Employee):
    def __init__(self, id):
        super().__init__(id)
        self.edit_language()
        self.edit_exp()

        attrs_counter = len(self.editable_attrs)

        self.editable_attrs[attrs_counter] = self.edit_language
        self.editable_attrs[attrs_counter + 1] = self.edit_exp

    def print(self):
        super().print()
        print("Язык программирования: {0}".format(self.language))
        print("Стаж программирования: {0}".format(self.exp))

    def edit_language(self):
        self.language = input("Введите язык программирования сотрудника\n")

    def edit_exp(self):
        try:
            self.exp = int(input("Введите стаж программирования (лет)\n"))
            if self.exp < 0:
                raise Exception
        except:
            print("Ошибка! Введите положительное число")
            self.edit_exp()

    def print_attrs_for_edit(self):
        attrs_counter = super().print_attrs_for_edit() + 1
        print("{0}. Язык программирования".format(str(attrs_counter)))
        print("{0}. Стаж программирования".format(str(attrs_counter + 1)))
