# Rewriting Lab045_Task3_Max_of_Numbers.py (task on Nov 12th) using if..else condition
# The input we are expecting is float and not int
# Step1
# i/p-2 float numbers
# o/p-String message

# step2 -Rough logic
# if num1 > num2 :
# print num1
# else :
# print num2

# Step3-Actaul code
num1 = float(input("Enter the first number- num1 \n"))
num2 = float(input("Enter the  second number -num2 \n"))
if num1 >= num2:
    print("Max is :", num1)
else:
    print("Max is :", num2)

    #Step3-Edge cases-num1==num2 ,print either of them by putting num1>=num2.Already handled above.
# Suppose if user gives "ten" which is string ,teh rpogram errors out-This can only be handled with
# try and except which we will learn in future
# Negative value also needs to be handled -We will learn that in future