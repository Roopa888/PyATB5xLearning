# concatenation of strings
str1 = "This is a line "
print(str1)
print(type(str1))
#str1=str1+1#we will get the error-"TypeError: can only concatenate str (not "int") to str"
# solution is to covert 1 to str and then add to str1
str1=str1+str(1)
print(str1)
print(type(str1))
first_name="Roopa"
last_name="Sree"
full_name=first_name+" "+last_name
print(full_name)
print(type(full_name))