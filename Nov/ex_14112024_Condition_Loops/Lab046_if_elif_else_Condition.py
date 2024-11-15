# To find max among 3 numbers using if ..else..else condition
# Assume i/p are all integers
# Logic buliding
#Step#1
# i/p-->3 integers -num1,num2,num3 which are int
#o/p --->String and an int containing the max value
#Step2-Rough logic
# if num1>num2 and num1>num3,print num1 is max
#     else if num2>num1 and  num2>num3 ,print num2 is max
#     else print num3 is max
# take eg:5,3 and 2  & 10,12 and 11
# Step3-Actual code
num1=int(input("Enter the first num\n"))
num2=int(input("Enter the second num\n"))
num3=int(input("Enter the  third num\n"))
if num1>num2 and num1>num3:
    print("Max is ",num1)
elif   num2 > num1 and num2 > num3:
        print("Max is ", num2)
else:
    print("Max is ",num3)
