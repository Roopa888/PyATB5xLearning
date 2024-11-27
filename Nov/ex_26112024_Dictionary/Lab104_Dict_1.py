my_dict = {"name": "Bini",
           "role": "SDET",
           "age": 49, "experience": 3}
print(my_dict)
# Accessing Values`
print(my_dict["age"])
print(my_dict["name"])
# `Adding/Updating a Key-Value Pair`
my_dict["age"] = 90
print(my_dict)
# new key also can be added
my_dict["name2"] = "KL"
print(my_dict)
# - `Removing a Key: **del** my_dict[key]`-The del keyword removes the item with the specified key name:
del my_dict["name2"]
print(my_dict)
# The pop() method removes the item with the specified key name.ehavior wise same as that of del
my_dict.pop("age")
print(my_dict)

# Another way to create a dictionary is as below
student_info = dict(Student_name="Nithya", age=79, address="CA")
print(student_info)
# empty dictionary
student_info1 = dict()
print(student_info1)

# For normal For loop the return will be the keys of the dictionary
for x in student_info:
    print(x)
# To get  teh values of te Keys
for x in student_info:
    print(student_info[x])
# Loop through both keys and values, by using the items() function
print(student_info.items())
for key, value in my_dict.items():
    print(key, "--->", value)
# use the values() function to return values of a dictionary:Same keys() returns all the keys
print("NNNN")
for x in my_dict.values():
    print(x)
# for x in my_dict.keys():
#         print(x)
# get () will give the value of a key/Ther are different ways to accesss the key and values using functions
n1 = my_dict.get("name")
print(n1)
print("************")
for x in my_dict.keys():
    print(my_dict.get(x))
print("age" in my_dict)
print("name"in my_dict)# Check if Key Exists in Dictionary.Values cant be checked for existence
