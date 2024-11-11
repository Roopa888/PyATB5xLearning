# Write a program to take two user inputs and then add teh number and print the sum
#Do multiplication-> *
# and Division-> /
# And print the results in each case
# Logic buliding
#i/p--> 2 user inputs -num1 and num2 (Ask what type of input)-int
# o/p-->Determine o/p-->Sum-int ,Sub-int ,Mul-Int and div-float
# Step2
# Rough logic
# we use sum--->+
# sub---> -
# Mul---->*
# Div--->/
# Step3
num1=int(input("Enter the first number,num1"))
num2=int(input("Enter the second number .num2"))
print(type(num1))
print(type(num2))
#Here you will get error for substaction onwards as num1 and num2 is string and math operators -,*,/ etc won't work on those
# Solution is to  convert num1 and num2 to int before doing math operations.str-->int
#changed line 15 ,16 to do this conversion
print ("Sum is :",num1+num2)
print ("Sub is :",num1-num2)
print ("Mul is :",num1*num2)
print ("Div is :",num1/num2)

# line 22 to 25 can also be  printed after assigning them into a new variabel name
sum=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
print ("Sum is :",sum)
print ("Sub is :",sub)
print ("Mul is :",mul)
print ("Div is :",div)



# Same exercise suing float as input
num3=float(input("Enter the first number,num3"))
num4=float(input("Enter the second number .num4"))
print ("Sum is :",num3+num4)
print ("Sub is :",num3-num4)
print ("Mul is :",num3*num4)
print ("Div is :",num3/num4)