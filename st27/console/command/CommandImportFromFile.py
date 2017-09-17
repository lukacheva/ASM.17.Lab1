import pickle
from .AbstractCommand import AbstractCommand


class CommandImportFromFile(AbstractCommand):
    DEFAULT_FILE = 'st27/storage/dump'

    def invoke(self):
        file_name = self.DEFAULT_FILE
        f = open(file_name, 'rb')
        self._car_showroom.set_cars(pickle.load(f))
        f.close()
        print('data loaded from ' + file_name)
        print('----------')
