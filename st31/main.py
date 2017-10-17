from .RunJournal import RunJournal

journal = RunJournal()
commands = [
    ['Записать пробежку', journal.addARun],
    ['Записать марафон', journal.addAMarathon],
    ['Отредактировать запись', journal.editTheJournal],
    ['Удалить запись', journal.deleteARun],
    ['Вывести журнал на экран', journal.showTheJournal],
    ['Записать журнал в файл', journal.writeToFile],
    ['Прочитать журнал из файла', journal.readFromFile],
    ['Очистить журнал', journal.clearTheJournal],
    ['Выйти', None]
]

def main():
    while True:
        print('\nКоманды:')
        for j in range(0,9):
            print(j+1, ':', commands[j][0])
        
        k = int(input('Введите команду: '))
        if k == 9:
            break
        elif k > 0 and k < 9:
            print('')
            commands[k-1][1]()
        else:
            print('ОШИБКА: Нет такой команды!')
            
if __name__ == "__main__":
    main()
        