from Actor import Actor


class LeonardoDiCaprio(Actor):
    def __init__(self):
        super().__init__()
        self.has_oscar = False
        self.editing_attributes.append(self.enter_got_oscar)
        self.edit_message.append('[3] - give or oscar\n')
        self.printing_bio.append(self.print_has_oscar)

    def enter_got_oscar(self):
        state = input('Print anything to give oscar to %s:' % self.name)
        if state:
            self.has_oscar = True
        else:
            self.has_oscar = False

    def print_has_oscar(self):
        if self.has_oscar:
            print('Leo have got oscar.')
        else:
            print('Leo still have not got the oscar.')
