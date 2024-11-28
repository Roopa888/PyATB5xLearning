# Sort a dictionary by its values in descending order
# i/p--->my_dict = {"a": 3, "b": 1, "c": 2}


# o/p--->{b: 1 , c: 2 , a :3}
my_dict = {"a": 3, "b": 1, "c": 2}
#Logic
list1 = list(my_dict.values())
print(list1)
list1.sort(reverse=True)
print("Sorted")
print(list1)
sorted_dict = {}
#Logic
for x in list1:
    for key,val in my_dict.items():
       if my_dict[key]==x:
           print("key:",key,val)
           sorted_dict[key]=val
print("Sorted Dictionary")
print(sorted_dict)
