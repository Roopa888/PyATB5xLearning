from abc import ABC, abstractmethod


class Father(ABC):
    def __init__(self,name): #This initializer gets precedence over the inherited class
        self.name=name
    @ abstractmethod
    def loan(self):
        pass
class Son(Father):
    def loan(self):
        print("1 Lakh loan given ")
son_obj=Son()
son_obj.loan()


