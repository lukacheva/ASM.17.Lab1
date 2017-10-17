from .console.ConsoleHandler import ConsoleHandler
from .CarShowroom import CarShowroom


def main():
    car_show_room = CarShowroom()
    ConsoleHandler(car_show_room).start()
