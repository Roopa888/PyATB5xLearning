# decorators take the function and add soem extra behaviors to it (at start and end of the function
# 
def add_security(func):#func will be replaced by any function name that has the @add_security annotation before it
    def wrapper():
        print("Before starting the driving")
        print("Wear Helmet,dashcash,knee guards,gloves,glass")
        func()  # Here driving_scooty will get executed.
        print("After the driving")
        print("Secure driving.Return the items")
    return wrapper()
    #The @ add_security syntax is a shorthand for driving_scooty =  add_security(driving_scooty).
#So no need to call driving_scooty() as we do normally if we have annotation before it
@ add_security
def driving_scooty():
    print("Normal Function")
    print("I am driving a scooty")
    # for this function also we can use teh same annotation
@ add_security
def driving_ola_scooter():
    print("Driving Ola Scooter")