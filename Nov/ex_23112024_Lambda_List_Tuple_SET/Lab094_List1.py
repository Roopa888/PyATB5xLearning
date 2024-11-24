# List is a collection of items
# can of same data type or different data type
#Duplicate are allowed
# grocery List -  butter, bread, banana, paneer.
my_list=[1,2,3,4,5]
my_list2=[3,4,"Taniya","John","12.34"]
print(my_list)
print(my_list2)
print(my_list[0])
print(my_list[3])
print(my_list[4])
#print(my_list[5]) # Will give error as index starts from  0
my_list[0]="Jill"
my_list[2]="Jack"
print(my_list[0])
print(my_list[2])
print(my_list)
print("**********************")
# using  a for loop to see the elements in an array
for item in my_list2:
    print(item)
print("**********************")
for item in range(1,5): # range actually returns a list .That's why we use the list directly when list is created
    print(item)