from st30.BookShop import BookShop
from st30.function import *


def main():
	book_shop = BookShop()
	menu = {
		"1": ['Add a book', book_shop.add_book],
		"2": ['Add a classbook', book_shop.add_classbok],
		"edit": ['Edit book', book_shop.edit_book],
		"show": ['Show base', book_shop.show_base],
		"write": ['Write to file', book_shop.write_file],
		"read": ['Read from file', book_shop.read_file],
		"clear": ['Clear the base', book_shop.clear_shop],
		"menu": ['Show menu'],
		"exit": ['Exit']
	}
	show_menu(menu)
	while (True):
		item = input('Select menu item\n')
		if str.lower(item) == "exit":
			break
		for i in menu:
			if ('menu' == str.lower(item)):
				show_menu(menu)
				break
			elif str.lower(i) == str.lower(item):
				menu[i][1]()


if __name__ == "__main__":
	main()
