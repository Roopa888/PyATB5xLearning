#  Remove duplicate values from a dictionary.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
# Output: {'a': 1, 'b': 2, 'd': 3}
# use set
unique_value=set()
result_dict={}
for key,value in my_dict.items():
    if value not in unique_value:
        result_dict[key]=value
        unique_value.add(value)
print("Dictionary after removing duplicates :")
print(result_dict)