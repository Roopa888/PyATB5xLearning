# Bulitin functions are functions that are available with Pythin already which the user can reuse
import math

print(math.pow(2,4)) # here math.pow is a function ,print itself is another function by Python guys
#Some eg:s below
print(str.lower("SUPER FAST"))
#str.upper()
print(max(2,9,-10))
#min()
#input()
n= int(input("Enter the number to be printed\n"))
print(n+1)
# user defined functions -written by user ..definition and calling by the user
def say_hello():
    print("Hello! Welcome")
say_hello()