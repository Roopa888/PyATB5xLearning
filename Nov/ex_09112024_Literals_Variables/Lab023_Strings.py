# characters in single quotes and double quotes are both considered as strings in Python
name=input("Enter the name:")
print(name)
print(type(name))
name1='c'
name2="C"
print("name1 is: ",name1)
print(type(name1))
print("name2 is :",name2)
print(type(name2))
name3='Welcome  to  Python learning'
print("name3 is :",name3)
print(type(name3))
name4="Welcome  to  Selenium learning"
print("name4 is :",name4)
print(type(name4))
#To find the length of a charcter use len() function.Length always starts from 1 and go on with 2,33...on.
print(len(name))
print("Upper case ",name.upper())
print("Lower  case ",name.lower())