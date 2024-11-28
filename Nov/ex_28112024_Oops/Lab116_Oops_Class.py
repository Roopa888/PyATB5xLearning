# declaration of class
class Person:
    # Attribute -What you have
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behavior member functions-What you can do
    def talk(self):  # No arg .no return self will be the first argument in every behavior
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am sleeping", name)

    def sleep2(self, name):  # Arg with Return
        print("I am sleeping -2")
        return None

    def walk(self):
        print("Start walking")

    def walk_return(self):  # No Arg with Return
        return "Walk-return"
# Create an object of the class
#ObjectRef = ClassName() -> Object
Geeta=Person()
Geeta.name="Geetha Sharma"
Geeta.gender="Female"
# Accessing object attributes
print(Geeta.name)
print(Geeta.gender)
print(Geeta.age)# default valeu assigned
# Invoking object method
print("Method calling")
print("*************")
Geeta.walk()
Geeta.sleep(Geeta.name)
str1=Geeta.walk_return()
print(str1)