# Task #1
#
# Write a program to take a user age and let him know if he can go the club.  Taake age=21
# Step1:
# i/p=user_age
# o/p=message -2 types of messages depending on the condition
# Step2:Rough logic
# if age>21 :
#     print("You can go to the club")
# else:
#     print("You can't go to the club")
# step3-Actual coding
user_age = int(input("Enter the user age\n"))
print("Yaay.You can go to the club" if user_age >=21 else "You can't go to the club")
