from time import perf_counter

student_inform = {"name": "Manu", "age": 78, "address": "KA"}
print(student_inform)

# update the age
student_inform["age"] = 14
print(student_inform)
# Nested dictionary
student_inform1 = {"name": "Jaya",
                   "age": 13,
                   "address": {
                       "home address": "Goa",
                       "Office address": "CA"
                   }
                   }
student_inform2 = {"name":"Ameya",
                   "age": 12,
    "address": {
    "home address": "Lahore",
    "Office address": "LA"
}
}

# make the two dict as 2 lists
student_list=[student_inform1,student_inform2]
print(student_list)
# To access each and evry element of teh student_list
print("Access each and evry element of teh student_list")
print(student_list[0])#-->1st dict
print(student_list[1])#--->second dict
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["home address"])
print(student_list[1]["address"]["Office address"])

# Alternate way to print directly from teh dictionary
print(student_inform2["address"]["Office address"])