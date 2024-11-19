# Write a program ,take a username and say hello to him
user_name=input("Enter the user name\n")
#function to say hello to the input user name
def say_hello_to_user(name):
    print("Hello",name)
# can we use the same variable name in input statement and function def liek below ?.Doubt to clarify .
#But it is wokring fine in both case (diffrent var names as well)
# def say_hello_to_user(user_name):
#     print("Hello", user_name)
#user_name=input("Enter the user name\n")
say_hello_to_user(user_name)
# Def always shoudl coem first before a function call or otherwise we get an error
# def say_hello_to_user(user_name):
#     print("Hello", user_name)

