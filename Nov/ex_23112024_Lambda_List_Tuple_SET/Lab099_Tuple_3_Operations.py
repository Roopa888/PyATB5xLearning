cities=("London","Paris","Los Angeles","London")
print("Paris" in cities)
print("New Delhi" in cities)
print("PARIS" in cities) #--->FALSE (case sensitive)

t = (12, 34, 56)
#t.append(58) # AttributeError: 'tuple' object has no attribute 'append'
# Convert the tuple to list and append an  element and convert it back to tuple
my_list2=list(t)
my_list2.append(4)
t=tuple(my_list2)
print("Appended to list and converted:",t)

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)# print as tuple