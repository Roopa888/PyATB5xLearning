# User defined functions -4 types
# 1. `The can't return -> non return`
# 2. They can return something
# 3. They have parameters
# 4. `They don't parameters / arguments`
import math


#1. They can't return -> non-return`-They don't have arguments /parameters .Do not  return any values
#no "return " keyword
def greet():
    print("Hello Function type1")

greet()

# 3. They have parameters.Take parameters but do not return any values,no "return " keyword

def greet_to_user(name):
    print("Hello",name)
greet_to_user("Kavitha")

# There is another type of function -No return type but with argument and the argument can  have a default value
#Also called as "positional arguments
def greet_to_defuserarg(name="Friend"):
    print(name.upper())
greet_to_defuserarg("Samudhra")
greet_to_defuserarg()

# Multiple default arguments examples below
def mult_user_args(name1="Joe",name2="Joseph"):
    print("Mult Args-->",name1,name2)
# Calling with different ways
print("++++++++++++")
mult_user_args()
mult_user_args(name1="Kate")
mult_user_args(name1="Kathy",name2="Jim")
mult_user_args(name2="Krista")
mult_user_args("Popy")
mult_user_args("Helen","Peter")
#math.pow() #ctrl +click -#You will see the similar implementation as in multi args
# Functions with arguments and return type-return keyword
# The below example does not have any default value
# Please note that we don't have to define the type of function in any definition unlike in Java
def sum_of_two_numbers(num1,num2):
    print("Sum")
    return num1+num2
result1=sum_of_two_numbers(25,30)
print(result1)
# example of Functions with default arguments and return type
def sum_of_two_numbers_default_args(num1=50,num2=100):
    #print("Sum")
    return num1+num2
print("Results with default arguments")
result2=sum_of_two_numbers_default_args(60,34)
result3=sum_of_two_numbers_default_args()
result4=sum_of_two_numbers_default_args(num1=70,num2=50)
print(result2)
print(result3)
print(result4)
# def addition_num(): #Not sure if these kind of functions are useful(No arguments but will return values
#     a=67
#     b=31
#     return a+b
# result5=addition_num()
# print(result5)
