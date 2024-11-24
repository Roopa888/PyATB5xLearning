from time import perf_counter

t=tuple() # create a new tuple
print(t)
#Conversion of List to tuples
t1=tuple(["Amit","Bevin","Jaysri","Hayne"])
print(t1)

#tuple of tuples
hero1=("Batman","Black Man")
hero2=("Wonder Woman","Diana Princess")
new_tuple=(hero1,hero2)
print(new_tuple)
# To access each element in the new_tuple
print("Access each element in the tuple-new_tuple")
print("******************************************")
print("First tuple:",new_tuple[0])
print("Second tuple:",new_tuple[1])
print("First element in hero1:",new_tuple[0][0])
print("Second element in hero1:",new_tuple[0][1])
print("First element in hero2:",new_tuple[1][0])
print("Second element in hero2:",new_tuple[1][1])