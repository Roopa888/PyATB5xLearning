# use of pass keyword in function is as below
def first_last_name():
    pass  # means the user will write the code in future (implement in the future .Pass acts just as a placeholder now for this function


# unctions within functions

def greet_all_of_you():
    print("Hello everyone")


def greet_2():
    print("Yes")
    greet_all_of_you()  # calling greet_all_of_you() inside the greet_2()

# greet_all_of_you()
greet_2()
