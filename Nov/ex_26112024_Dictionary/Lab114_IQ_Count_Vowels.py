input_string = " happy birthday to all"
# a,e, i,o,u.
vowels = "aeiou"
vowel_count = 0
result = dict()
for char in input_string:
    if char in vowels:
        vowel_count = vowel_count + 1
        match char:
            case "a":
                result[char] = result.get(char, 0) + 1
            case "e":
                result[char] = result.get(char, 0) + 1
            case "i":
                result[char] = result.get(char, 0) + 1
            case "o":
                result[char] = result.get(char, 0) + 1
            case "u":
                result[char] = result.get(char, 0) + 1
            case _:  # default
                pass
print(vowel_count)
print(result)

