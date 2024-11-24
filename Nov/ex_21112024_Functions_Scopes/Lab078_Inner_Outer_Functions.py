# inner functions can always access teh variable in their resp outser functions
# outer functions
def outer_function():
    var1 = 30

    def inner_function1():
        var2=89
        print(var1)
        print(var2)

    def inner_function2():
        print(var1)
    ##print(var2)  #var2 is local to inner_function1 .So it cannot be accessed outside that function
    inner_function1() # for the 2 inner functions ,var1 act as a global variable as the functions are already inside the outer_function
    inner_function2()



outer_function()
# Suppose if we change the indendation,it will be an outside function and can no longer
#  access var1 of outer_function
#For others  it is a local variable and gloabl variable only to its inner functions
# def inner_function3():
#     print(var1)
# inner_function3()
