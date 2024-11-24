# Tuple --->collection of items
# Immutable

my_tuple = (1, 4, 9, 16, 25)
print(my_tuple)
# my_tuple[5]=88  # Error-TypeError: 'tuple' object does not support item assignment

# list is used when are sure that the items  in the collections may change
# For eg:if we want to change "paneer" with "milk"

shopping_list = ["bread", "Butter", "Jam", "Paneer"]
print(shopping_list[3])
shopping_list[3] = "Milk"
print(shopping_list[3])
print(shopping_list[3])

# Real use of tuples
my_tuple = ("tta.com", "sdet.live")
my_api_list = list(my_tuple)
print(my_api_list)
# my_tuple[0]="abc.com" # cant directly assign any items to tuple like in list .Have to convert the tupel into list and add them
my_api_list[0] = "abc.com"
print(my_api_list)
conv_tuple = (tuple(my_api_list))
print(conv_tuple)
# conv_tuple[0]="Lemon"
# if we convert the list to tuple and try to add ,again we can't be additional elements
# if we just print it using type conversion the list can  be used to add additional elements
print((tuple(my_api_list)))
my_api_list[1] = "nmb.com"
print(my_api_list)
print(my_tuple)

# Real case, where we Tuples -->API URLs mostly won't change
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[1])