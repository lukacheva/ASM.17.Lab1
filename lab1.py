import st00.main
import st01.main
import st02.main
import st03.main
import st05.main
import st12.main
import st23.lab1
import st39.main
import st16.main
import st27.main
import st35.main
import st38.main
import st29.main
import st07.main
import st24.main
import st31.main
import st42.main
import st17.main
import st33.main
import st22.main

#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main

MENU = [
        ["[00] Образец", st00.main.main],
        ["[01] Абдуллатипова", st01.main.main],
        ["[02] Аганов", st02.main.main],
        ["[03] Антипов", st03.main.main],
        ["[05] Баганов", st05.main.main],
        ["[07] Белова", st07.main.main],
        ["[12] Вайланд", st12.main.main],
        ["[23] Ишмаметьев", st23.lab1.main],
        ["[39] Тимошин", st39.main.main],
        ["[16] Гаврилов", st16.main.main],
        ["[24] Кондрат", st24.main.main],
        ["[27] Ларионов", st27.main.main],
        ["[35] Проценко", st35.main.main],
        ["[38] Солопеева", st38.main.main],
        ["[29] Макарик", st29.main.main],
        ["[31] Николаева", st31.main.main],
        ["[42] Худояров", st42.main.main],
        ["[17] Григорян", st17.main.main],
        ["[33] Платов", st33.main.main],
        ["[22] Иванов", st22.main.main],

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
