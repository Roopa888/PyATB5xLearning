from time import perf_counter


class Dog:
    #-Attributes-member variables
    name=None
    breed=None
    height=None
    weight=None

# Behavior-Member functions
    def bark(self):
        print("Barking")

    def sleep(self):
        print("sleep")

    def talk(self):
        pass
# Object Ref
chow = Dog()
# Dog() - Object
# chow -> Object Ref.
bow=Dog()
mow=Dog()
ranchow=Dog()
ranchow.talk()# no o/p since it is a pass
print("Bow's name is ",bow.name)
print("Mow barking")
mow.bark()