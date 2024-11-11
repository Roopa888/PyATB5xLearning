# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1
num1=input("Enter the number to be divided: ")
num2=input("Enter the number to be used for dividing num1")
#We get error "TypeError: unsupported operand type(s) for divmod(): 'str' and 'str'" if we just don't convert the input str to int
num1=int(num1)
num2=int(num2)
print("The quotient and Remainder after divsion are :",divmod(num1,num2))