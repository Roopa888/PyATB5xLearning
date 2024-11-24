# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Answer
def first_non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None


print("The first non_repeating character---->",first_non_repeating_char("swiss"))
print("The first non_repeating character---->",first_non_repeating_char("MANAMA"))
print("The first non_repeating character---->",first_non_repeating_char("COCOCOLA"))
print("The first non_repeating character---->",first_non_repeating_char("DADA"))
print("The first non_repeating character---->",first_non_repeating_char("LAKALAKENENLA"))
print("The first non_repeating character---->",first_non_repeating_char("CAMECA"))

# The same program when taken as input string
# s1 = input("Enter the string to be checked\n")
# print("The first non_repeating character---->", first_non_repeating_char(s1))


# using set

# def first_non_repeating_char_using_sets(string):
#     seen = set()
#     unique1 = set()
#
#     for char in string:
#         if char in seen:
#             continue
#         if char in unique1:
#             unique1.remove(char)
#             seen.add(char)
#         else:
#             unique1.add(char)  # seen for the first time ,add to unique_1
#             #print(unique1)
#     return unique1 if len(unique1) == 1 else None
#
#
# print(first_non_repeating_char_using_sets("ABABAS"))
# print(first_non_repeating_char_using_sets("LAKALAKENENLA"))
# print(first_non_repeating_char_using_sets("CAMECA"))

