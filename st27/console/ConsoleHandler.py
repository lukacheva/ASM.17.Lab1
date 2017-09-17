from ..AbstractCarShowroom import AbstractCarShowroom
from .command.CommandAddCar import CommandAddCar
from .command.CommandShowCars import CommandShowCars
from .command.CommandAddUsedCar import CommandAddUsedCar
from .command.CommandEditCar import CommandEditCar
from .command.CommandClear import CommandClear
from .command.CommandExportToFile import CommandExportToFile
from .command.CommandImportFromFile import CommandImportFromFile
from .command.CommandDeleteCar import CommandDeleteCar


class ConsoleHandler:
    __EXIT_COMMAND_KEY = '0'

    def __init__(self, car_showroom: AbstractCarShowroom):
        self.__command_map = {
            '1': {'description': 'Show cars', 'handler': CommandShowCars},
            '2': {'description': 'Add car', 'handler': CommandAddCar},
            '3': {'description': 'Add used car', 'handler': CommandAddUsedCar},
            '4': {'description': 'Edit car', 'handler': CommandEditCar},
            '5': {'description': 'Delete car', 'handler': CommandDeleteCar},
            '6': {'description': 'Export to file', 'handler': CommandExportToFile},
            '7': {'description': 'Import from file', 'handler': CommandImportFromFile},
            '8': {'description': 'Clear', 'handler': CommandClear}
        }
        self.__car_showroom = car_showroom

    def __print_command(self, key: str, description: str):
        print(key + ". " + description)

    def print_command_map(self):
        for key in self.__command_map:
            command = self.__command_map[key]
            self.__print_command(key, command['description'])
        self.__print_command(self.__EXIT_COMMAND_KEY, 'Exit')

    def start(self):
        self.print_command_map()
        self.listen()

    def listen(self):
        command_key = input(">")

        if command_key == self.__EXIT_COMMAND_KEY:
            return

        try:
            command_data = self.__command_map[command_key]
            command_handler = command_data['handler']
            command = command_handler(self.__car_showroom)
            command.invoke()
        except Exception as e:
            print('Exception was thrown: ', e)

        self.start()
