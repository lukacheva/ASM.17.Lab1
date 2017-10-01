from .Book import Book


class Classbook(Book):
	subject = ''
	type = 'Classbook'
	edit_menu = []

	def __init__(self):
		m = ["subject", self.set_subject]
		Book.__init__(self, m)

	def set_subject(self):
		self.subject = input('Enter the subject to be learned using the book\n')

	def book_registration(self):
		Book.book_registration(self)
		self.set_subject()

	def show_book(self):
		Book.show_book(self, self.type)
		print('Subject: ' + self.subject)
