try:
    num1=int(input("Enter the num1\n"))
    num2=int(input("Enter the num2\n"))
    result1=num1/num2

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Result: ",result1) # els ewill execute if ther eis no exception in try block

# try:
#     num1 = int(input("Enter the num1\n"))
#     num2 = int(input("Enter the num2\n"))
#     result = num1 / num2
#     print(result)
# except Exception as e:
#     print(e)
