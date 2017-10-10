class Horses:

	def __init__(self, name, age, color, breed):
		
		self.input_data()
		
		self.name = name
		self.age = age
		self.color = color
		self.breed = breed
		
	def input_data(self):
	
        self.name = input('Введите имя лошади: ');	
		self.age = input('Введите возраст лошади: ');
		self.color = input('Введите масть лошади: ');
		self.breed = input('Введите породу лошади: ');		
		
	def print_horse(self):

		print(self.name, self.age, self.color, self.breed)