from .platform import *

platform = Place()

menu = {"1": ("Добавить оборудование", platform.add_rig),
        "2": ("Добавить модифицированное оборудование", platform.add_modified_rig),
        "3": ("Редактировать", platform.edit),
        "4": ("Удалить", platform.delete),
        "5": ("Вывести список на экран", platform.display_atribut),
        "6": ("Сохранить список в файл", platform.write),
        "7": ("Загрузить список из файла", platform.read),
        "8": ("Очистить список", platform.clean_out),
        "9": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 9:
            break
        menu[user_input][1]()
