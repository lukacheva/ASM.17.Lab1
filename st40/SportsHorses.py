from .Horses import Horses

class SportsHorses(Horses):
	
	def __init__(self, name, age, color, breed, type_of_sport):
		
		self.input_data()
		
		self.type_of_sport = type_of_sport
	
		
	def input_data(self):
	
        self.type_of_sport = input('Введите вид спорта лошади: ');	
			
		
	def print_horse(self):

		print(self.name, self.age, self.color, self.breed, self.type_of_sport,)