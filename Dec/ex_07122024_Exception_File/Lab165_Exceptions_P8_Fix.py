# line 2,3 amd 4 all are vulnerable for excpetions-value error ,zero divison error etc
# we will fix it using the try ..excpet block
print("----Start of the program")
try:
    a=int(input("Enter the num1 :"))
    b=int(input("Enter the num2 :"))
    c=a/b
    print("Result of the div is ", c)
except Exception as e:
    print(e)

print("----End of the program")