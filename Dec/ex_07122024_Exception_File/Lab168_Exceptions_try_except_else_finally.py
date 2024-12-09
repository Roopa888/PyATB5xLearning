try:
    num1 = int(input("Enter the num1:\n"))
    num2 = int(input("Enter the num2:\n"))
    result = num1 / num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Result is :",result)
finally:
    print("This block always will get executed whther program is executed successfully  or failed")
