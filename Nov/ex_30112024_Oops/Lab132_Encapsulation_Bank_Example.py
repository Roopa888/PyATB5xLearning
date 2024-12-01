class Bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.balance = balance

    def check_balance(self):
        print("Balance is :", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_account_number(self, auth):
        if auth == True:
            print("Account number is : ", self.__account_number)
        else:
            print("Not Authorised")

    def __internal_private_method(self):
        print("Private methid  can only be accessed by class ,not by objects as it calss other member functions")
    def test1(self):
        self.__internal_private_method()

icici = Bank(99000213, 23000)
icici.deposit(500)
icici.check_balance()
print(icici.balance)
# print(icici.__account_number) # AttributeError: 'Bank' object has no attribute '__account_number'. Did you mean: '_Bank__account_number'?
# Encapsulation allows us to access the private variables only through functions
icici.show_me_account_number(False)
# Advantage -We can add auth so that only the authorised person can see the data .Dat will be hidden from unauthorised persons
#icici.__internal_private_method()
icici.test1() # only test can access this function as it belongs to same class