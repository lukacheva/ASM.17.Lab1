from .Book import Book


class Classbook(Book):
	__subject = ''
	__edit_menu = []

	def __init__(self):
		m = ["subject", self.set_subject]
		Book.__init__(self, m)

	def set_subject(self):
		self.__subject = input('Enter the subject to be learned using the book\n')

	def book_registration(self):
		Book.book_registration(self)
		self.set_subject()

	def show_book(self):
		Book.show_book(self)
		print('Subject: ' + self.__subject)
