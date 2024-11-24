import math


def find_power(num):
    return (math.pow(num,2))
print(find_power(3))

op2=lambda: math.pow(int(input("Enter the number to find power for:\n")),3)
print(op2())