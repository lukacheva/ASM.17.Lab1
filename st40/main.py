from .Stable import Stable

HorseStable = Stable()

item = {"1":(" - Добавление лошади", HorseStable.new_horse),
		"2":(" - Вывести список всех лошадей", HorseStable.write_all_horse), "3":(" - Очистка списка лошадей", HorseStable.clean_all_horse ),
		"4":(" - Запись списка в файл", HorseStable.write_to_file),"5":(" - Загрузка списка из файла", HorseStable.read_from_file),
		"6":(" - Выход", None)}
def main():
    while True:
        print('  Главное меню:')
        for k in range(1,7):
            print(k,"-",item[str(k)][0])
        i = input()
        if int(i)==6:
            break
        if int(i)>=1 and int(i)<7:
            item[i][1]()
        else:
            print('Ошибка! Выберите номер от 1 до 7!')

if __name__ == "__main__":
    main()
