# SET -Collection of unique elements
# non repeatable elements
# No order maintained for the elements
#{}=parenthesis
list_unique_elements={1,2,3,4,4,5,5}
print(list_unique_elements)   # Result--> {1, 2, 3, 4, 5}.4 and 5 printed only once

# list and SET
list1=[45.2,33,33,45,46,2,2,1]
set1=set(list1)
print("List1 --->",list1) # duplicates allowed
print("Set1---->",set1) # duplicates not allowed

# tuple and SET
tuple1=("TheTestingAcademy","Online","TheTestingAcademy","Udemy","TheTestingAcademy")
print("Tuple1--->",tuple1) # duplicates allowed
print("Set from the tuple",set(tuple1)) # duplicates not allowed

