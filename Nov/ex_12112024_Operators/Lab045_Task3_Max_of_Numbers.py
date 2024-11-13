# Task 3
# Problem to find the max between two ( 3,4) → 4
# Step1
from colorsys import yiq_to_rgb

# i/p-num1 and num2 -int
# o/p-int-greaternum
# using ternary operator
# greater_num=num1 if num1 > num2 else num2
# print result

# Actual code
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
greater_num = num1 if num1 > num2 else num2
print(f"The greater number among {num1} and {num2} is:{greater_num}")
