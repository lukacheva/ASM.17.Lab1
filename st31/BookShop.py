from .Book import Book
from .Classbook import Classbook
from .function import *
import pickle


class BookShop():
	__base = []

	def add_book(self):
		book = Book()
		book.book_registration()
		self.__base.append(book)

	def add_classbok(self):
		classbook = Classbook()
		classbook.book_registration()
		self.__base.append(classbook)

	def show_base(self):
		print("\nThe assortment of the store includes " + str(len(self.__base)) + " books\n")
		for i in range(len(self.__base)):
			print(str(i + 1))
			self.base[i].show_book()

	def edit_book(self):
		self.show_base()
		while (True):
			key = input("Select the book number for editing\n")
			if is_int(key) and 0 < int(key) <= len(self.__base):
				self.__base[int(key) - 1].edit_book()
				break
			else:
				print("Books under this number do not exist")
				answer = input('Want to repeat again?\nYes/No')
				if (str.lower(answer) != 'yes'):
					break

	def write_file(self):
		file_name = input('Enter file name\n')
		with open(str(file_name) + '.dat', 'wb') as f:
			pickle.dump(self.__base, f)
		print('The file is successfully recorded')

	def read_file(self):
		while (True):
			file_name = input('Enter file name\n')
			if (is_file(file_name)):
				with open(str(file_name) + '.dat', 'rb') as f:
					self.__base = pickle.load(f)
					self.__base()
				break
			else:
				print('Error reading the file')
				answer = input('Want to repeat again?\nYes/No')
				if (str.lower(answer) != 'yes'):
					break

	def clear_shop(self):
		self.__base = []
		print('Base successfully cleared!')
