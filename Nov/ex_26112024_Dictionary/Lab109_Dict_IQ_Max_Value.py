# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}
# Logic
# i/p-dictionary
# find teh max value return that value
my_dict = {"a": 10, "b": 20, "c": 30}
def find_max_value(dict):
    return max(dict.values())
    #return min(dict.values())

print("Max value is ", find_max_value(my_dict))
