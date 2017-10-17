from .part3 import *

aut = autopark()

menu = {"1": ("Добавить информацию о машине", aut.add_car),
        "2": ("Добавить полную информацию о машине", aut.add_fcar),
        "3": ("Редактировать", aut.edit),
        "4": ("Удалить", aut.dlt),
        "5": ("Вывести список на экран", aut.show_data),
        "6": ("Сохранить список в файл", aut.wrtf),
        "7": ("Загрузить список из файла", aut.rff),
        "8": ("Очистить список", aut.clear_data),
        "9": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 9:
            break
        menu[user_input][1]()
