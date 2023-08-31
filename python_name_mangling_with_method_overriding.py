class Employee:
    def __init__(self, name):
        self.name = name
        self.__getData()

    def getData(self):
        print(f"{self.name}")

    __getData = getData

class Programmer(Employee):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        self.__print()

    @staticmethod
    def print():
        print("Programmer Class")
        
    @staticmethod
    def __print():
        print("Programmer Class")

    __print = print

obj = Programmer("Rishabh")
obj.print()
obj._Programmer__print()