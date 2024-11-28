# Question 2 :
# my_list = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates from a list using a set.
# Output: [1, 2, 3, 4, 5]
my_list = [1, 2, 2, 3, 4, 4, 5]
print(my_list)
set1=set(my_list)
print(set1)
conv_list=list(set1)
print("The list after removing duplicates :")
print(conv_list)