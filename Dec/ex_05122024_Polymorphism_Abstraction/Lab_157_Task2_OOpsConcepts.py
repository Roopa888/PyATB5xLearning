from abc import ABC, abstractmethod


class BankAccount():
    def __init__(self, acc_num, acc_bal):
        self.__acc_num = acc_num
        self.balance = acc_bal


class ICICIAccount(BankAccount):
    def withdraw(self):
        print("Money withdrew")
    @abstractmethod
    def loan(self):
        pass
    @staticmethod
    def customercare():
        print(" Calling Customer care")
ic1=ICICIAccount(122,40000)
ic1.withdraw()
ic1.customercare()
ic1.loan()