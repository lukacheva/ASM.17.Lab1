class Candidate:
    """Класс, описывающий соскателя без опыта работы"""
    def __init__(self):
        self.set_first_name(input('Введите имя соискателя: '))
        self.set_last_name(input('Введите фамилию соискателя: '))
        self.set_gender(input('Введите пол соискателя: '))
        self.set_age(input('Введите возраст соискателя: '))
        self.set_mail(input('Введите E-mail соискателя: '))
        
    def __str__(self):
        self.print = f"Имя соискателя: {self.first_name} | Фамилия соискателя: {self.last_name} | Пол соискателя: {self.gender} | Возраст соискателя: {str(self.age)} | E-mail соискателя: {self.mail}"
        return self.print
            
    # методы, позволяющие считывать атрибуты объета класса с консоли    
    def set_first_name(self, from_console):
        self.first_name = from_console

    def set_last_name(self, from_console):
        self.last_name = from_console

    def set_gender(self, from_console):
        self.gender = from_console

    def set_age(self, from_console):
        self.age = from_console
        
    def set_mail(self, from_console):
        self.mail = from_console
        
    # метод, позволяющий редактировать атрибуты объекта класса
    def edit(self):
        self.set_first_name(input('Введите имя соискателя: '))
        self.set_last_name(input('Введите фамилию соискателя: '))
        self.set_gender(input('Введите пол соискателя: '))
        self.set_age(input('Введите возраст соискателя: '))
        self.set_mail(input('Введите E-mail соискателя: '))
        
    # методы, позволяющие считать атрибуты объекта класса                            
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_mail(self):
        return self.mail



