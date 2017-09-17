import st00.main
import st23.lab1
import st39.main
import st16.main
import st27.main

#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main

MENU = [
        ["[00] Образец", st00.main.main],
        ["[23] Ишмаметьев", st23.lab1.main],
        ["[39] Тимошин", st39.main.main],
        ["[16] Гаврилов", st16.main.main],
        ["[27] Ларионов", st27.main.main],

#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]

def menu():
	print("------------------------------")
	for i, item in enumerate(MENU):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

try:
	while True:
		MENU[menu()][1]()
except Exception as ex:
	print(ex, "\nbye")
