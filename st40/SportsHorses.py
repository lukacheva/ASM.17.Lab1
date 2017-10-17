from .Horses import Horses

class SportsHorses(Horses):
	
	def __init__(self):
#			print("__init__ sport")
			self.input_data()
		
	def input_data(self):
			Horses.input_data(self)
			self.type_of_sport = input('Введите вид спорта лошади: ');
		
	def print_horse(self):
			print(self.name, self.age, self.color, self.breed, self.type_of_sport,)