def add_decor1(func):
    def wrapper():
        print("Inside decor1")
        func()
        print("Exited decor1")
    return wrapper


def add_decor2(func):
    def wrapper():
        print("Inside decor2")
        func()
        print("Exited decor2")
    return wrapper


@add_decor1
@add_decor2
def say_Hello():
    print("Hello!Welcome")


say_Hello()

#order will be as below
# Inside decor1
# Inside decor2
# Hello!Welcome
# Exited decor2
# Exited decor1