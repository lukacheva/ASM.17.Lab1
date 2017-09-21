from .customers import *

def add(customers):
    print("Нажмите 1 для добавления обычного клиента")
    print("Нажмите 2 для добавления vip клиента")
    typeadd = input(" >>  ")
    try:
        add_actions[typeadd](customers)
    except KeyError:
        print("Ошибка ввода! Попробуйте еще\n")
        add_actions['add'](customers)    
    return

def client(customers):
    client = Client()
    customers.add(client)
    return

def vipclient(customers):
    vipclient = Vipclient()
    customers.add(vipclient)
    return

add_actions = {
    'add': add,
    '1': client,
    '2': vipclient
}


def edit(customers):
    if len(customers) < 1:
        print("Список пуст\n")
    else:
        print("Выберите клиента для редактирования \n")
        print(customers)
        try:
            customers.edit(int(input("Введите номер >>  "))-1)
        except (ValueError, IndexError):
            print("Ошибка ввода!\n")
            edit(customers)   
    return

def delete(customers):
    if len(customers) < 1:
        print("Список пуст\n")
    else:
        print("Выберите клиента для удаления\n")
        print(customers)
        try:
            customers.delete(int(input("Введите номер >>  "))-1)
        except (ValueError, IndexError):
            print("Ошибка ввода!\n")
            delete(customers)
    return

def print_customers(customers):
    print(customers)


def save(customers):
    customers.save()   
    print("Сохранено\n")

def load(customers):
    customers.load()
    print("Загружено\n")

    
def clear(customers):
    customers.clear()
    print("Очищено\n")
    return

def exit(customers):
    return

customers = Customers()

def main():    
    print("Меню")
    print("1. Добавить клиента")
    print("2. Редактировать клиента")
    print("3. Удалить клиента")
    print("4. Вывести список")
    print("5. Очистить")
    print("6. Сохранить в файл")
    print("7. Загрузить из файла")    
    print("0. Выход")
    choice = input(" >>  ")
    menu(choice)

 
def menu(choice):
    try:
        menu_actions[choice](customers)
    except KeyError:
        print("Ошибка ввода\n")
    if choice != '0':       
        menu_actions['main']()


menu_actions = {
    'main': main,
    '1': add,
    '2': edit,
    '3': delete,
    '4': print_customers,
    '5': clear,
    '6': save,
    '7': load,
    '0': exit,
}
 
if __name__ == "__main__":
    main()