from .exp_candidate import *
import pickle

class Data_Base:

    def __init__(self):
        self.data_base = []

    def __len__(self):
        return len(self.data_base)
   
    def __str__(self):
        output_list = ''
        index = 1
        if len(self.data_base) < 1 :
            return 'Список пуст!'
        else:
            for element in self.data_base:
                output_list = output_list + str(index) + '. ' +  str(element) + '\n'
                index += 1
            return output_list
        
    def add(self, candidate):
        self.data_base.append(candidate)

    def edit(self, index):
        self.data_base[index - 1].edit()

    def clear_list(self):
        self.data_base.clear()

    def save_to_file(self):
        pickle.dump(self.data_base, open("st13/candidates.p", "wb" ))

    def load_from_file(self):
        self.data_base = pickle.load(open("st13/candidates.p", "rb" ))

 
