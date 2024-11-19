# Predict the o/p for the following case
def sum_three(a=1,b=1,c=1):
    return a+b+c

result1=sum_three()
print(result1)
result2=sum_three(1,2)
print(result2)
result3=sum_three(1,2,3)
print(result3)
result4=sum_three(a=67,b=10,c=45)
print(result4)
# The belwo will give error as the number of arguments is  not matching
#result5=sum_three(10,20,30,40) #
# result5=sum_three(a=10,b=89,c=90,67)
# print(result5)