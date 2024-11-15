# write a program to take user age as input and let him know if he can go to club
# Take age limit as 21
# Logic building fromula
# Step#1
# i/p-data type-->int
# o/p-data type-->String -message to the user

# Step#2 Rough logic (brutr force logic)
# age >21--->print can go to club
# age<21--->print can't go to club

# Step #3-Write the code logic
age = input("Enter the age \n")
age = int(age)
if age >= 21:
    print("Yaay.You can go to the club")
else:
    print("Sorry.You can't go to the club")

# Step#4-Check for edge cases
# Edge case -The input at which teh program will break
# Negative ages or extremely high values for age
# When age is 21 or -22 and on it gives "can't go to club" message
# Exteremely high values also handled by Python but it is better to give an agen below 125
# that means that is handled,so no code is needed to test this edge
# Non-numeric input-ABC-string cant be given
# Age which is valid -For eg:it is not sensible to give age-200 or above 125 or so .So this case
# needs to be handled


# Step#5-Optmize teh code-->means we will handle all the possible edge cases(TBD)
