# Union,Intersection,difference
set1={1,2,3,4,5}
set2={4,5,6,7,8}
my_set=set1.union(set2)
print(f"Set 1 union set2--->{my_set}")

my_set=set1.intersection(set2)
print(f"Set1 intersection set2--->{my_set}")


my_set=set1.difference(set2)# elements in set1 which are not in set2
print(f"Set1 difference set2--->{my_set}")
my_set=set2.difference(set1) # elements in set2 which are not in set1
print(f"Set2 difference set1----->{my_set}") 