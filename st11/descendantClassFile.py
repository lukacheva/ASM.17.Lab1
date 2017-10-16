from  .myClassFile import myClass

class descendantClass(myClass):
    def __init__(self):
        super().__init__()
        print("Введите параметр")
        self.additionalAttribute=input()
        print("Введите второй паареметр")
        self.secondAdditionalAttribute=input()
        
    def printAdditionalAttribute(self):
        print( self.additionalAttribute)
        
    def printSecondAdditionalAttribute(self):
        print(self.secondAdditionalAttribute)
        
    def writeAdditionalAttribute(self):
         print("Введите параеметр")
         self.additionalAttribute=input()
         
    def writeSecondAdditionalAttribute(self):
        print("Введите второй паареметр")
        self.secondAdditionalAttribute=input()
