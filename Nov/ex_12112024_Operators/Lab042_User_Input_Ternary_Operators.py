# Program if age>18 ,then allowed to vote
# else not allowed to vote
user_age=int(input("Enter your age\n"))
# if user_age>18:
#     print("Yes ,you can go and vote")
# else:
#     print("No you can't go and can't vote")

# doing using Ternary operator
print("Yes ,you can go and vote" if user_age>18 else "No you can't go and can't vote" )

# All of the above (line no: 3 and 10 )can be done in one line but not recommended.Just replace user_age input line in if condition like below

print("Yes ,you can go and vote" if int(input("Enter your age\n"))>18 else "No you can't go and can't vote" )
# Even line10 -Ternary operators are never recommended use (use if else instead) as it reduces  code readability