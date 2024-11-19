# function
# identifier rules will have to be followed for function names as well
# A few examples below

# def 123():
#     print("Function Name with 123")
#
#
# 123()  # Will give "SyntaxError: invalid syntax" because the function name identifier cant start with a number

# The below is a valid name for function

def _123():
    print("Function Name with _123")
_123()


# The below is a valid name for function

def _():
    print("Function Name with _")
_()

# The below is a valid name for function
def Roop123():
    print("Function Name with Roop123")
Roop123()
# The below is a valid name for function
# The line of codes inside a function should  ahve to be intended properly
#Otherwise it will be considered a line outside the function

def h():
    print("Function Name with h")
    print("This is part of h function")
print("This is not part of h function.It is outside of the function h as the intendation has changed ")
h()
h()
