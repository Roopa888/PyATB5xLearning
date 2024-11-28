# Take input and create a class in python
# We can modify the default_init constructor to ta atke the input from user which can be used to create teh class
# Define another function which will display the details of class when object instantiation is done
# i/p-name,age,phone ,occupation
class Person:
    def __init__(self):
        self.name = input("Enter the name:\n")
        self.age = input("Enter the age:\n")
        self.phone = input("Enter the phone:\n")
        self.occupation = input("Enter the occupation:\n")

    def display_Object_details(self):
        print(f"Name is --->{self.name}", f"Age is --->{self.age}", f"Phone is --->{self.phone}",
              f"Occupation is ---> {self.occupation}")

person1=Person()
person1.display_Object_details()
