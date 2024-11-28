# Using  parameterised constructor for the program in Lab121_Class-Calc_Non_PC -Calc

class Calc:
    # parameterised constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Other functions
    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

# if we want the i/p to be taken from the user line23 to 30 and then insatiate the object with parameters(line25)
# a = float(input("Enter the value of a:\n"))
# b = float(input("Enter the value of b:\n"))
# object_ref2 = Calc(a, b)
# print("*****************")
# print(object_ref2.sum())
# print(object_ref2.sub())
# print(object_ref2.mul())
# print(object_ref2.div())

# Direct parametrised call for init
object_ref3=Calc(9,3)
output_sub3=object_ref3.sub()
print(output_sub3)

output_sub3=object_ref3.sum()
print(output_sub3)