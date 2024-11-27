input_string = "hello, world!"
# a,e, i,o,u.
vowels = "aeiou"
vowel_count = 0
result = dict()
n=0
for char in input_string:
    if char in vowels:
        vowel_count = vowel_count + 1


print(vowel_count)
print(result)