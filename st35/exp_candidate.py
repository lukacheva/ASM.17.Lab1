from .candidate import *

class Exp_Candidate(Candidate):

    def __init__(self):
        Candidate.__init__(self)
        self.set_experience(input('Введите опыт работы соискателя: '))
        self.set_last_job(input('Введите предыдущее место работы соискателя: '))

    def __str__(self):
        Candidate.__str__(self)
        return f"{self.print} | Опыт работы соискателя: {self.experience} | Предыдущее место работы соискателя: {self.last_job}"

    # методы, позволяющие считывать атрибуты объета класса с консоли           
    def set_experience(self, from_console):
        self.experience = from_console

    def set_last_job(self, from_console):
        self.last_job = from_console
        
    # метод, позволяющий редактировать атрибуты объета класса   
    def edit(self):
        Candidate.edit(self)
        self.set_experience(input('Введите опыт работы соискателя: '))
        self.set_last_job(input('Введите предыдущее место работы соискателя: '))
    # методы, позволяющие считать атрибуты объета класса
    
    def get_experience(self):
        return self.experience

    def get_last_job(self):
        return self.last_job

