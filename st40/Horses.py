class Horses:

	print("Horses: ")	
		
	def __init__(self):
		print("__init__")
		self.input_data()
		
	def input_data(self):
			print("input_data")
			self.name = input('Введите имя лошади: ');	
			self.age = input('Введите возраст лошади: ');
			self.color = input('Введите масть лошади: ');
			self.breed = input('Введите породу лошади: ');		
		
	def print_horse(self):

		print(self.name, self.age, self.color, self.breed)