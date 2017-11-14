﻿import st00.main
import st01.main
import st02.main
import st03.main
import st05.main
import st07.main
import st09.main
import st10.main
import st12.lab1
import st13.main
import st16.main
import st17.main
import st18.main
import st19.main
import st20.main
import st21.main
import st22.lab1
import st23.main
import st25.main
import st26.main
import st27.main
import st28.main
import st30.main
import st31.main
import st32.main
import st33.main
import st34.main
import st35.main
import st36.main
import st37.main
import st38.main
import st39.main
import st40.main
import st41.main
import st42.main


#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main

MENU = [
        ["[00] Образец", st00.main.main],
        ["[01] Абдуллатипова", st01.main.main],
        ["[02] Аганов", st02.main.main],
        ["[03] Антипов", st03.main.main],
        ["[05] Баганов", st05.main.main],
        ["[07] Белова", st07.main.main],
        ["[09] Беркита", st09.main.main],
        ["[10] Бледных", st10.main.main],
        ["[12] Бреткин", st12.lab1.main],
        ["[13] Вайланд", st13.main.main],
        ["[16] Гаврилов", st16.main.main],
        ["[17] Григорян", st17.main.main],
        ["[18] Гюлмамедов", st18.main.main],
        ["[19] Джамалов", st19.main.main],
        ["[20] Зубарева", st20.main.main],
        ["[21] Иванов", st21.main.main],
        ["[22] Ишмаметьев", st22.lab1.main],
        ["[23] Кондрат", st23.main.main],
        ["[25] Кысылбаиков", st25.main.main],
        ["[26] Ларионов", st26.main.main],
		["[27] Лукачева", st27.main.main],
        ["[28] Макарик", st28.main.main],
        ["[30] Николаева", st30.main.main],
        ["[31] Паньшина", st31.main.main],
        ["[32] Платов", st32.main.main],
        ["[33] Попова", st33.main.main],
        ["[34] Проценко", st34.main.main],
        ["[35] Сидоренко", st35.main.main],
        ["[36] Синалицкий", st36.main.main],
        ["[37] Смирнов", st37.main.main],
        ["[38] Солопеева", st38.main.main],
        ["[39] Тимошин", st39.main.main],
        ["[40] Федорова", st40.main.main],
        ["[41] Фраткин", st41.main.main],
        ["[42] Худояров", st42.main.main],

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
