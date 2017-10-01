from .function import *


class Book:
	title = ''
	cost = 0
	publishing_house = ''
	author = ''
	type = 'Book'
	edit_menu = []

	def __init__(self, m=[]):
		self.edit_menu = {
			"1": ['title', self.set_title],
			"2": ['cost', self.set_cost],
			"3": ['publishing_house', self.set_publishing_house],
			"4": ['author', self.set_author]
		}
		if len(m):
			self.edit_menu["5"] = m

	def set_title(self):
		self.title = input('Enter book title\n')

	def set_cost(self):
		while (True):
			cost = input('Enter the cost of the book\n')
			if (is_float(cost)):
				self.cost = cost
				break
			else:
				print('Warning. Enter float')

	def set_publishing_house(self):
		self.publishing_house = input('Enter the publishing house of the book\n')

	def set_author(self):
		self.author = input('Enter the author of the book\n')

	def book_registration(self, type='none'):
		print(self.type if type == 'none' else type)
		self.set_title()
		self.set_cost()
		self.set_publishing_house()
		self.set_author()

	def show_book(self, type='none'):
		if (type == 'none'):
			type = self.type
		print(type + '\nTitle: ' + self.title + '\n' + 'Cost: ' + str(
			self.cost) + '\n' + 'Publishing house: ' + self.publishing_house + '\n' + 'Author: ' + self.author + '\n')

	def edit_book(self):
		for i in self.edit_menu:
			print(i + ' - ' + self.edit_menu[i][0])
		while (True):
			key = input("Select a field for editing\n")
			if is_int(key) and 0 < int(key) <= len(self.edit_menu):
				self.edit_menu[key][1]()
				break
			else:
				print('Error. This field does not exist')
				answer = input('Want to repeat again?\nYes/No')
				if (str.lower(answer) != 'yes'):
					break
