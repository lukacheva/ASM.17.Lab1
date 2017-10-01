from .catalog import *

def stop():
    return 1

catalog = Catalog()

MENU = [
        ['Добавить новый автомобиль', catalog.add_new],
        ['Добавить подержанный автомобиль', catalog.add_used],
        ['Показать каталог', catalog.show_catalog],
        ['Редактировать каталог', catalog.edit_catalog],
        ['Удалить автомобиль', catalog.delete_auto],
        ['Очистить каталог', catalog.clear_catalog],
        ['Сохранить каталог', catalog.save_catalog],
        ['Загрузить каталог', catalog.load_catalog],
        ['Выход',stop]
    ]

def main():
    while True:
        print('Меню')
        i = 1
        for item in MENU:
            print("{0}) {1}".format(i, item[0]))
            i += 1
        try:
            var = int(input("\nВвод: "))
            if MENU[var-1][1]():
                return
        except:
            print('Ошибка ввода\n')
        
if __name__ == '__main__':
    main()
