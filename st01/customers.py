from .vipclient import *
import pickle
class Customers:
    def __init__(self):
        self.customer = []
    def add(self, x):
        self.customer.append(x)
    def edit(self, num):
        self.customer[num].edit()
    def delete(self,num):
        self.customer.pop(num)
    def clear(self):
        self.customer = []
    def save(self):
        pickle.dump( self.customer, open( "st01/pickledata.p", "wb" ) )
    def load(self):
        self.customer = pickle.load( open( "st01/pickledata.p", "rb" ) )
    def __len__(self):
        return len(self.customer)
    def __str__(self):
        string = ''
        count = 1
        if self.customer:
            for e in self.customer:
                string =string + str(count) +". " + str(e) + "\n"
                count +=  1          
        else:
            string="Список пуст\n"
        return string