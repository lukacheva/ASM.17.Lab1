import pickle
from .AbstractCommand import AbstractCommand


class CommandExportToFile(AbstractCommand):
    DEFAULT_FILE = 'st27/storage/dump'

    def invoke(self):
        if self._car_showroom.is_empty():
            print('car showroom is empty')
            print('----------')
            return

        file_name = self.DEFAULT_FILE
        f = open(file_name, 'wb')
        pickle.dump(self._car_showroom.get_all(), f)
        f.close()
        print('data dumped to ' + file_name)
        print('----------')
