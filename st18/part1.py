class infcar:
    def __init__(self):
        self.mark = None
        self.color = None
        self.year = None

    def read(self):
        self.mark = input("Введите марку автомобиля:")
        self.color = input("Введите цвет автомобиля:")
        self.year = input("Введиет год автомобиля:")

    def write(self):
        print("Марка автомобиля: " + self.mark)
        print("Цвет автомобиля: " + self.color)
        print("Год автомобиля: " + self.year)
