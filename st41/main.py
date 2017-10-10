from .Music import *
import os
OP=Music()
MENU = [
        ["Добавить отечественного исполнителя", OP.AddNative],
        ["Добавить зарубежного исполнителя", OP.AddForeign],
        ["Вывести список на экран", OP.ShowList],
        ["Записать список в файл", OP.WriteToFile],
        ["Считать список из файла", OP.ReadFromFile],
        ["Очистить список", OP.ClearList],
        ["Редактировать элемент", OP.ChangeAlbum],
        ["Удалить элемент списка", OP.DeleteAlbum],
        ["Выход"]
    ]
def main():
    print("------------------------------")
    for i, item in enumerate(MENU):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    kot = int(input("ввод: "))
    if kot != 8:
        MENU[kot][1]()
        main()

if __name__ == "__main__":
        try:
                main()
        except:
                print("неверный ввод")
