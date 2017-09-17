from .AbstractCommand import AbstractCommand


class CommandClear(AbstractCommand):
    def invoke(self):
        self._car_showroom.clear()
        print('----------')
