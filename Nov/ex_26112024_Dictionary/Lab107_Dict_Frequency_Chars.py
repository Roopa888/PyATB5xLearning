# Frequency of Characters in a String
# Write a program to count the frequency of each character in a given string.
# Logic :
# ip-string
# o/p---> dict with values {char:no of occurrences}
# I/P - string e.g automation
# O/P -> dict  # {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}
#string = "automation"
string =input("Enter the input string:\n")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
