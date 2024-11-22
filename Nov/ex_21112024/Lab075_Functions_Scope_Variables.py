# Golbal variable
pb_global_b=19 #global variable
def my_function():
    pb_a=10 #local variable
    print(pb_a)
    print(pb_global_b)
# print(pb_a) # cannot be cald outside function .We get name 'pb_a' is not defined  error
print(pb_global_b) #This can be printed outside as it is global variable
my_function()