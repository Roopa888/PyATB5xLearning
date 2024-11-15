# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
from encodings.undefined import Codec
from tokenize import String
from unittest.mock import AsyncMock

# Logic building
# Step1
# i/p-->score-data type-->int(float usually get rounded to int in case of score)
# o/p- grade--A or B-->String
score = int(input("Enter your score\n"))
# Step2-Rough logic
# score >= 90 and <= 100 - -->grade A
# score >= 80 and <= 89 - -->grade B
# score >= 70 and <= 79 - -->grade C
# score >= 60 and <= 69 - -->grade D
# score >= 0 and <= 59 - -->grade F
if score >= 90 and score <= 100:
    print("Your grade is :A")
elif score >= 80 and score <= 89:
    print("Your grade is :B")
elif score >= 70 and score <= 79:
    print("Your grade is :C")
elif score >= 60 and score <= 69:
    print("Your grade is :D")
elif score >= 100 or score<=-1:# You have to handle this condition as the
    # user can give more than 100 as score and then thsi program may give a wrong o/p
    # -ve numebrs can also be handled in this way with "or" condition
    print("You are superb.You can't get a score!!!")
else:
    print("Your grade is :F")
