for i in range(1, 10, 2):
    print(i)
# if we don't give start value ,the default value is zero.Step valeu is optional,default is 1)
print("---------------")
for i in range(10):
    print(i)

    # If we don't pass anything in range ,it will error out
    # TypeError: range expected at least 1 argument, got 0

# for i in range():
#     print(i)
    #Using negavtive values for range
    print("Negative values")
for i in range(-10,-1):
    print(i)
print("Negative values with step")
for i in range(-10,-1,2):
    print(i)
    #We can go backwards also if we give step as negative
print("Going backwards with step")
for i in range(-1, -10, -1):
    print(i)