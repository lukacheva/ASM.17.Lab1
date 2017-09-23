import pickle

from .emploee import Employee
from .developer import Developer

class Company:
    employees = []

    def add(self):
  
        ids = list(map(lambda e: e.id, self.employees))
        if len(ids) > 0:
            next_id = max(ids) + 1
        else:
            next_id = 1
        employee_type = input("Кого вы хотите добавить?\n1.Обычный сотрудник\n2.Разработчик\n")
        if employee_type == "1":
            employee = Employee(next_id)
        else:
            if employee_type == "2":
                employee = Developer(next_id)
            else:
                print("Ошибка! Неверный тип сотрудника")
                self.add()
                return
        self.employees.append(employee)

    def edit(self):
        employee = self.get_employee()
        if employee is not None:
            employee.edit()

    def remove(self):
        employee = self.get_employee()
        if employee is not None:
            self.employees.remove(employee)

    def print(self):
        for employee in self.employees:
            employee.print()

    def clear(self):
        self.employees.clear()

    def serialize(self):
        with open('company.txt', 'wb') as f:
            pickle.dump(self.employees, f)

    def deserialize(self):
        with open('company.txt', 'rb') as f:
            self.employees = pickle.load(f)

                
    def get_employee(self):
        try:
            id = int(input("Введите номер сотрудника, которого вы хотите отредактировать\n"))
        except:
            print("Ошибка! Введите число")
            self.get_employee()
            return
        employees = [e for e in self.employees if e.id == id]
        if len(employees) == 0:
            print("Сотрудника с таким номером не существует")
            return
        else:
            return employees[0]
