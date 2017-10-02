from .function import *


class Book:
	__title = ''
	__cost = 0
	__publishing_house = ''
	__author = ''
	__edit_menu = []

	def __init__(self, m=[]):
		self.__edit_menu = {
			"1": ['title', self.set_title],
			"2": ['cost', self.set_cost],
			"3": ['publishing_house', self.set_publishing_house],
			"4": ['author', self.set_author]
		}
		if len(m):
			self.__edit_menu["5"] = m

	def set_title(self):
		self.__title = input('Enter book title\n')

	def set_cost(self):
		while (True):
			cost = input('Enter the cost of the book\n')
			if (is_float(cost)):
				self.__cost = cost
				break
			else:
				print('Warning. Enter float')

	def set_publishing_house(self):
		self.__publishing_house = input('Enter the publishing house of the book\n')

	def set_author(self):
		self.__author = input('Enter the author of the book\n')

	def book_registration(self):
		print(str(self.__class__.__name__))
		self.set_title()
		self.set_cost()
		self.set_publishing_house()
		self.set_author()

	def show_book(self):
		print(str(self.__class__.__name__) + '\nTitle: ' + self.__title + '\n' + 'Cost: ' + str(
			self.__cost) + '\n' + 'Publishing house: ' + self.__publishing_house + '\n' + 'Author: ' + self.__author + '\n')

	def edit_book(self):
		for i in self.__edit_menu:
			print(i + ' - ' + self.__edit_menu[i][0])
		while (True):
			key = input("Select a field for editing\n")
			if is_int(key) and 0 < int(key) <= len(self.__edit_menu):
				self.__edit_menu[key][1]()
				break
			else:
				print('Error. This field does not exist')
				answer = input('Want to repeat again?\nYes/No')
				if (str.lower(answer) != 'yes'):
					break
