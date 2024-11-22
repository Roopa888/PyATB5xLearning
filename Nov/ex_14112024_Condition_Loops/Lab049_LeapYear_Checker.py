# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.


# Logic Building
# Step 1
# i/p-Year-->int
# o/p-Message --->String
year = int(input("Enter the year to be checked\n"))

# Step2-Rough Logic
# year%4>0--->Not a leap year
# year%4==0 and year%100==0 and year%400==0--->Leap Year
# year%4==0 and year%100==0 and year%400>0--->Not a leap year
print(year % 4)
print(year % 100)
print(year % 400)
# Actual code
if (year%4==0 and year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
            print(f"Year {year} is  a leap year")
else:
            print(f"Year {year} is not a leap year")
#    #############-From Nov19 session coding using functions
# def check_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
#
#
#
# if check_leap_year(year):
#     print("Yes")
# else:
#     print("No")