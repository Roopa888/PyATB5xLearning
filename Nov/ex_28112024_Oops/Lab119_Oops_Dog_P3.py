# How constructors are getting called when object is created
# It enables us to create the object with it specific attributes by passing those attributes
# as parameters to the constructors(parameterised constructors)
# Otherwise we will just get an object as mentioned in the class e.g"name=None" if default constructor is used
# Or if we change name="Chow" and call Dog() with  2 objects ,2 object's name will be Chow which will be in correct way of initializing
# Controls our Object Instantiation

class Dog:
    #Attributes
    name=None
    breed=None
    height=None
    weight=None
    # name
    # breed
    # height
    # weight
# modify the default constructor.if it is not modified the default will be called
#     def __init__(self):
#         print("I will be called")


# Behavior-methods
    def bark(self):
        print("Bark")
    def sleep(self):
        print("Sleep")
    def talk(self):
        pass

# Object reference
chow_ref=Dog()
Mow_ref=Dog()

print(chow_ref.name) # Now  will be printed as None is given as attribute initial value
print(Mow_ref.name)   # will give error if we don't assign name=None.'name' is not defined