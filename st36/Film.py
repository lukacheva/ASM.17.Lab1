from .Actor import Actor
import pickle


class Film:
    def __init__(self):
        self.enter_film_name()
        self.actors = {}

    def enter_film_name(self):
        self.film_name = input('Enter new film name: ')

    def print_film_name(self):
        print('Film name is %s' % self.film_name)

    def print_all_actors(self):
        for name, actor_object in self.actors.items():
            actor_object.print_name()

    def add_new_actor(self):
        new_actor = Actor()
        self.actors[new_actor.name] = new_actor

    def edit_actor(self):
        print('Type name of actor you want to edit: ')
        for actor_name, actor_object in self.actors.items():
            print(actor_name)
        actor_name = input()
        self.actors[actor_name].edit_bio()

    def remove_actor(self):
        print('Type name of actor you want to remove: ')
        for actor_name, actor_object in self.actors.items():
            print(actor_name)
        actor_name = input()
        self.actors.pop(actor_name)

    def remove_all_actors(self):
        self.actors.clear()

    def save_actors_to_file(self):
        with open('Film.txt', 'wb') as f:
            pickle.dump(self.actors, f)

    def load_actors_from_file(self):
        with open('Film.txt', 'rb') as f:
            self.actors = pickle.load(f)