# FizzBuzz Test
# Write a program that prints numbers from 1 to 100.
# However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz." ( for, if)
# Logic building
# Step 1:
# i/p-->don't have to give .Just print  1 ro 100
# O/p-List of numbers with Fizz and Buzz for numbers divisible by 3 and 5 respectively
# Step2 -Rough Logic
# for numbers 1 to 100,do the following
# if number%3==0 and number%5==0,print "FizzBuzz"
# if number%3==0 ,print "Fizz"
# if number%5==0 ,print "Buzz"
# else print teh number
# Step3-Actual Logic
i, j, k = 0, 0, 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        i += 1
    elif number % 3 == 0:
        print("Fizz")
        j += 1
    elif number % 5 == 0:
        print("Buzz")
        k += 1
    else:
        print(number)
# To know the number of items in each category,printed the below
print("===============")
print("No: of FizzBuzz:", i)
print("No: of Fizz:", j + i)
print("No of Buzz:", k + i)
# Number divisible by 3 and 5 between 1 and 100 are ---> 15 30 45 60 75 90
# Number divisible by 3  between 1 and 100 are --->3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48
# 51 54 57 60 63 66 69 72 75 78 81 84 87 90 93 96 99
# Number divisible by 5  between 1 and 100 are--->5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
# for number in range(1, 101):
#     if number % 5 == 0:
#         print(number, end=" ")
