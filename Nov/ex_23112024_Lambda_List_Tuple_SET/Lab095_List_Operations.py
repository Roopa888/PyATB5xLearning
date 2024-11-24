my_list = [1, 2, 3]
# Append-Append object to the end of the list.
my_list.append(40)
print(my_list)
print(my_list[3])
list2=[600,6,6]
#my_list.append(40,50) # thsi will give error "takes exactly one argument (2 given)"
# print("CCCCC")
# my_list.append(list2) # o/p-[1, 3, 'Wow', 40, [600, 6, 6], 6, 7, 8, 9]/here it is list inside list not liek extend

# extend() - Append a new list.Duplicates are allowed.Takes a single list as an argument
my_list.extend([6, 6, 7, 8, 9])
print(my_list)

# insert()--->inserts an element at a specified index in a list
my_list.insert(3, "Wow")
print(my_list[3])
print(my_list)
my_list[1] = "Dayana"
print(my_list)
print(my_list[1])

# remove()---->remove one element from the list
my_list.remove("Dayana")
print(my_list[1])
print(my_list)
print(len(my_list))
# copy a list
print("*********************************")
my_copy_list = my_list.copy()
print(my_copy_list)

my_copy_list.remove(40)
print("ppppppp")
print(my_list)
print(my_copy_list)
my_list.remove(6)
print("Removed 6 from  my_list")
print(my_list)
print(my_copy_list)
# sort() the list
print("Sort")
print(my_list)
my_list.remove('Wow')  # sort usually applies to only string or int and not of different types
my_list.sort(reverse=True) #descending order
print(my_list)
my_list_2=["Jas","Giri","Yono","Farah","Aby"]
print(my_list_2)
my_list_2.sort()
print(my_list_2)