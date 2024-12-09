# Custom exceptions .Creat eusing Exception as base class
"""
Exception raised for custom error scenarios.
    Attributes:
        message -- explanation of the error
"""
class LowBalanceException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)


balance = 100
withdraw = int(input("Enter the amount to be withdrawn :\n"))
if withdraw > balance:
    raise LowBalanceException("Your balance is low")
else:
    print("Your balance is updated to :",balance-withdraw)


