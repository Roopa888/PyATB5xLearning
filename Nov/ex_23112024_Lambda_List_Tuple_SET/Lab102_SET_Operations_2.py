# Unique elements are inclcuded (even with slight differences
set1=set(["TheTestingAcademy","Udemy","TheTestingAcademy.","Course era","Course era","LinkedIn"])
print("Elements in set1 ---->",set1) #"TheTestingAcademy" and "TheTestingAcademy." are different since there is a dot the end of 2nd element
print("No of elements in the set",len(set1)) # length after eliminating teh duplicates will be the result.Here it is 5 not 6

# Iterate through teh set elements
for i in set1:
    print(f"Element--->{i}")

set1.add("KOLKATTA")
print(set1)
set1.add("KOLKATTA") # "Same string will not be added twice but here no error will come when we run the program