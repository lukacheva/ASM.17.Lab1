from tkinter import *
from .dinner import *

dinner=dinner()

def Блюдо():
    dinner.add_food()

def Напиток():
    dinner.add_drink()

def Запись():
    dinner.write()

def Чтение():
    dinner.read()

def Вывод():
    dinner.all_()

def Очистить():
    dinner.clear()

def Редактировать():
    dinner.edit()

def main():
    root = Tk()
    root.title('Меню')
    root.geometry('600x500')

    main = Menu()
    add_menu = Menu()
    add_menu.add_command(label = 'Блюдо', command=Блюдо)
    add_menu.add_command(label = 'Напиток', command=Напиток)

    file_menu = Menu()
    file_menu.add_command(label = 'Запись в файл', command=Запись)
    file_menu.add_command(label = 'Чтение из файла', command=Чтение)

    main.add_cascade(label = 'Добавить', menu=add_menu)
    main.add_command(label = 'Вывести всю картотеку', command=Вывод)
    main.add_cascade(label = 'Файл', menu=file_menu)
    main.add_command(label = 'Редактировать', command=Редактировать)
    main.add_command(label = 'Очистить', command=Очистить)

    root.config(menu=main)

    root.mainloop()






