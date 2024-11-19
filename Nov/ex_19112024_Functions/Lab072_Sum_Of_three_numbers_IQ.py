# Create a program to find the sum of three numbers from user inputs
# if the user does not enter any number,use default numbers as 100,200 and 300
def sum_of_3_numbers(num1=100, num2=200, num3=300):
    return num1 + num2 + num3



num1 = int(input("Enter the first number-num1 \n"))
num2 = int(input("Enter the second number-num2 \n"))
num3 = int(input("Enter the third number-num3 \n"))
result1 = sum_of_3_numbers(num1, num2, num3)
print(result1)
result2 = sum_of_3_numbers() #  as of now if we dont give any input (Press enter for  num1)in this program
# it will give error  since we are now not handling it with try ...catch
# "ValueError: invalid literal for int() with base 10: ''
print(result2)
# Advantage of having the default arguments is -you can have teh function with 1 ,2 or 3 functions
# (if all values are not provided it will take the default arguments and gives the results .Flexible
result4=sum_of_3_numbers(num1=400)
print(result4)