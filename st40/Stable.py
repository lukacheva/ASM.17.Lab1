


class Stable:
	all_horses = []

	def f(self):
		print("st00.Stable.f()")
		
	def new_horse(self):
        horse = Horses()
        self.all_horses.append(horse)
        print("\n New horse added")
