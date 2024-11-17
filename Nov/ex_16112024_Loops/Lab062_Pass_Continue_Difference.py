# The program to highlight the diffrence between pass and continue
# Using pass
for i in range(10):
    if i==7:
        pass # This will just pass and then teh print statement will also come under the if condition
        print(i)


print("+++++++++")
# Using pass
for i in range(10):
    if i==7:
        continue # This will just continue execution with For loop  and then the print statement will not (also come under the if condition) be executed
        print(i)