from descendantClassFile import descendantClass
from myClassFile import myClass
import pickle


class classContainer:
    # classList = []
    def __init__(self):
        self.classList = list()

    def addClass(self):
        classExemplar = myClass()
        self.classList.append(classExemplar)

    def addDescendantClass(self):
        classExemplar = descendantClass()
        self.classList.append(classExemplar)

    def editClassParam(self):
        print("Введите порядковый номер элемента списка")
        i = input()
        print("Введите новое имя2")
        self.classList[int(i)].name = input()
        print("Введите новый параметр")
        self.classList[int(i)].param = input()

    def showList(self):
        for i in range(0,len(self.classList)):
            print(self.classList[i].name)

    def readListFromFile(self):
        with open("1.txt", "rb") as file:
            self.classList = pickle.load(file)

    def writeListInFile(self):
        with open("1.txt", "wb") as file:
            pickle.dump(self.classList, file)

    def clearList(self):
        self.classList.clear()
