from .Horses import Horses
from .SportsHorses import SportsHorses
import pickle
print("Stable")

class Stable:
	all_horses=[]
	def __init__(self):
		print("__init__ Stable")
				
	def new_horse(self):
			print("Введите '1', чтобы создать лошадь или введите '2', чтобы создать спортивную лошадь: ")
			i=input()
			if int(i)==1:
				horse=Horses()
				#horse.__init__()
				self.all_horses.append(horse)
				print("\n New horse added")
			else:
				sport_horse = SportsHorses()
				#sport_horse.__init__()
				self.all_horses.append(sport_horse)
				print("\n New sport horse added")
				
	def write_all_horse(self):
			j = 0
			print("write_all_horse")
			while j < len(self.all_horses):
				self.all_horses[j].print_horse()
				j = j+1
	
	def write_to_file(self):
			file = open("all_horses.dat", "ab")
			pickle.dump(self.all_horses, file)
			file.close()
				
	def read_from_file(self):
			file = open("all_horses.dat", "rb")
			self.all_horses = pickle.load(file)
			self.write_all_horse()
			file.close()
				
	def clean_all_horse(self):
			self.all_horses.clear()
			print('Список лошадей очищен.')