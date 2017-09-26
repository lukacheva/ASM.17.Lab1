from .Library import *

_library = Library()

MENU = [
    ["Добавить пользователя(гость)", _library.add_Guest],
    ["Добавить пользователя(студент)", _library.add_Regustered],
    ["Редактировать данные пользователя", _library.edit_student],
    ["Удалить пользователя", _library.del_student],
    ["Вывод списка на экран", _library.print_list],
    ["Запись списка в файл", _library.in_file],
    ["Чтение списка из файла", _library.out_file],
    ["Очистить список", _library.clear_list],
    ["Выход"]
    ]

def menu():
    print("\tМеню:")
    for i, item in enumerate(MENU):
        print(i+1, item[0])
        
def main():
    menu()
    while True:
        try:
            index = int(input("\nEnter index, please >> "))
            if index == 9:
                break
            else:
                MENU[index-1][1]()
        except IndexError as ei:
            print("Неверный индекс", ei)
            menu()
        except Exception as e:
            print("Возникла исключительная ситуация", e)
            menu()

##        i = 1
##        for item in MENU:
##            print("{0}. {1}".format(i, item[0]))
##            i += 1
if __name__ == '__main__':
    main()
