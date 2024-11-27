# Create a dictionary from two lists below
# zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator
keys = ["name", "role", "experience"]
values = ["Aman", "SDET",3 ] # suppose the numbers are not matching ,only those keys will be there which has a value in the second
#res = zip(keys, values)
print(list(zip(keys, values))) # returns an iterator and then we have to convert it to list or dict to print
my_dict = dict(zip(keys, values))
print(my_dict)
#Merge two dictionaries
#The | operator combines dict1 and dict2 into d1 new dictionary d3.
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged_dict=dict1|dict2
print("The merged dictionary")
print(merged_dict)
print(merged_dict.get("a"))
# USing update function

d1={"a":1,"b":2}
d2={"b":3,"d":4}
d1.update(d2) # update d1 with d2 values .duplicate values are removed by retaining value of d2 for that key
print("The merged dictionary-Update d2")
print(d1)

