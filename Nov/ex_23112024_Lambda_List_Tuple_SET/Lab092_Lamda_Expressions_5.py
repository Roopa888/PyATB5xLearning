# Using Ternary operator in lambda expressions
# Multiple statements
# Write a program to calculate even and odd
def find_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


find_even_odd(90)
num2 =int (input("Enter the number you want to check\n"))
#check=lambda num: "Even"  if num%2==0 else "odd"
# check=lambda num: print ("Even")  if num%2==0 else print ("odd")
# check(num2) # Just have to call check like a function if print is within the lambda expression
# Have to call check like a function within print ()if print is not within the lambda expression
check=lambda num:  "Even"  if num%2==0 else  "odd"
print(check(num2))