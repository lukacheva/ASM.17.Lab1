from .squad import *

squad = Squad()

menu = {"1": ("Добавить воина", squad.add_warrior),
        "2": ("Добавить воина-мага", squad.add_mage),
        "3": ("Редактировать", squad.edit),
        "4": ("Удалить", squad.dlt),
        "5": ("Вывести список на экран", squad.show_spisok),
        "6": ("Сохранить список в файл", squad.wrtf),
        "7": ("Загрузить список из файла", squad.rff),
        "8": ("Очистить список", squad.clear_spisok),
        "9": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 9:
            break
        menu[user_input][1]()
