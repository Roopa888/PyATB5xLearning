# function without arguments
def say_hello():
    print("Hello")


say_hello()


# function without arguments .Here the variable name will be replaced with "Roopa" or "Shweta"
def say_hello_to(name):
    print("Hello", name)
    print(f"Hello to {name}")
say_hello_to("Roopa")
say_hello_to("Shweta")
say_hello_to(123) # The arguments can be of any data type .For eg:Here we used int and float
say_hello_to(3.14) #and float
