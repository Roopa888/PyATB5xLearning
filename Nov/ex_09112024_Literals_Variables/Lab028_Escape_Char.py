#escape sequence
# if we want to print something with \n or \d directly the system wont be able to do as it considers it as escape characters
# Eg : below.We will get syntax error ==>SyntaxWarning: invalid escape sequence '\P'
# dir="C:\Python\t.txt"
# print(dir)
# To fix this Python has introduced raw string so that it will print as it is even if \n or \t is present in string
dir2=r"C:\Python\t.txt"
print(dir2)
# Same for single quoted string and doubel quoted string
print(r"Preet'i\n\K")