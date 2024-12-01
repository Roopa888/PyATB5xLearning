# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Answer
# def first_non_repeating_char(string): #using a function
#     for char in string:
#         if string.count(char) == 1:
#             return char
#     return None
#
#
# print("The first non_repeating character---->",first_non_repeating_char("swiss"))
# print("The first non_repeating character---->",first_non_repeating_char("MANAMA"))
# print("The first non_repeating character---->",first_non_repeating_char("COCOCOLA"))
# print("The first non_repeating character---->",first_non_repeating_char("DADA"))
# print("The first non_repeating character---->",first_non_repeating_char("LAKALAKENENLA"))
# print("The first non_repeating character---->",first_non_repeating_char("CAMECA"))

# The same program when taken as input string
# s1 = input("Enter the string to be checked\n")
# print("The first non_repeating character---->", first_non_repeating_char(s1))


# using set
# def first_non_repeating_char_using_sets(string):
#     seen = set()
#     unique1 = set()
#     unique2 = set()
#     for char in string:
#         if char in seen:
#             continue
#         if char in unique1:
#             unique1.remove(char)
#             seen.add(char)
#         else:
#             unique1.add(char)  # seen for the first time ,add to unique_1
#     if len(unique1) > 1:
#         for char in string:
#             if char in unique1:
#                 first_non_rep=char
#                 unique1.clear()
#                 unique1.add(char)
#                 print("FIRST nR", unique1)
#                 break
#     return unique1 if unique1 else None
#
#
# print(first_non_repeating_char_using_sets("ABABAS"))
# print(first_non_repeating_char_using_sets("LAKALAKENENLA"))
# print(first_non_repeating_char_using_sets("CAMECA"))
# print(first_non_repeating_char_using_sets("CAMECAXZ"))
# print(first_non_repeating_char_using_sets("FANCOOLAN"))
# print(first_non_repeating_char_using_sets("WESTINDIES"))
# print("The first non_repeating character---->",first_non_repeating_char_using_sets("DADA"))

# using set and list
def first_non_repeating_char_list_set(string):
    seen2=set()
    unique2=[]
    for char in string:
        if char in seen2:
            continue
        if char in unique2:
            unique2.remove(char)
            seen2.add(char)
        else:
            unique2.append(char)

    return set(unique2[0]) if unique2 else None

print(first_non_repeating_char_list_set("ABABAS"))
print(first_non_repeating_char_list_set("LAKALAKENENLA"))
print(first_non_repeating_char_list_set("CAMECA"))
print(first_non_repeating_char_list_set("CAMECAXZ"))
print(first_non_repeating_char_list_set("FANFOOLA"))
print(first_non_repeating_char_list_set("WESTINDIES"))
print("The first non_repeating character---->",first_non_repeating_char_list_set("DADA"))