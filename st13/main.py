from .data_base import *

def print_map():
    for key, value in menu_map.items():
        print(f"{key} - {value}")

def candidate():
    candidate = Candidate()
    data_base.add(candidate)
    
def exp_candidate():
    exp_candidate = Exp_Candidate()
    data_base.add(exp_candidate)
    
def edit():
    identifier = int(input("Введите ID соискателя для редактирования: "))
    data_base.edit(identifier)
    
def print_db():
    print(data_base)

def clear():
    data_base.clear_list()

def save():
    data_base.save_to_file()
    print("Список успешно сохранён в файл")
    
def load():
    data_base.load_from_file()
    print("Список успешно загружен из файла")
    
def main():
    print_map()
    while True:
        cmd = int(input("Введите команду: "))   
        if cmd == 0:
            break
        else:
          menu.get(cmd)()
          
menu_map = {
        '1' : 'Добавить в список соискателя без опыта работы',
        '2' : 'Добавить в список соискателя c опытом работы',
        '3' : 'Редактировать выбранного соискателя',
        '4' : 'Вывести список соискателей на экран',
        '5' : 'Очистить список соискателей',
        '6' : 'Сохранить список соискателей в файл',
        '7' : 'Загрузить список соискателей из файла',
        '8' : 'Вывести меню на экран',
        '0' : 'Остановить программу'
}

menu = {
     1 :  candidate,
     2 :  exp_candidate,
     3 :  edit,
     4 :  print_db,
     5 :  clear,
     6 :  save,
     7 :  load,
     8 :  print_map
}

data_base = Data_Base()
    
if __name__ == "__main__":
    main()


