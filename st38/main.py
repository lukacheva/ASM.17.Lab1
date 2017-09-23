from .company import Company
 
def main():

    company = Company()

    menu = {
        "1": company.add,
        "2": company.edit,
        "3": company.remove,
        "4": company.print,
        "5": company.clear,
        "6": company.serialize,
        "7": company.deserialize,
    }
    
    EXIT_CODE = "8"

    while True:
        print()
        print("Выберите действие")
        print("1. Добавить сотрудника")
        print("2. Отредактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Просмотреть всех сотрудников компании")
        print("5. Очистить список сотрудников")
        print("6. Записать список сотрудников в файл")
        print("7. Считать список сотрудников из файла")
        print("8. Выход")
        user_input = input("\n");
        if user_input == EXIT_CODE:
           return   
        action = menu.get(user_input)
        if action is not None:
            action()
        else:
            print("Ошибка! Неверный пункт меню")
            continue


if __name__ == '__main__':
    main()


