#inheritance and methid override(polymorphism)
class Animal:
    def eat(self):
        return "Food they get "

    def sound(self):
        return "peculiar sound"

    def sleeps(self):
        return "Sleeps in Forest"


class Lion(Animal):
    def eat(self):  # single inheritance -overrides eat() and sleeps() of Animal class
        return "Meat"

    def sleeps(self):
        return "Den"


class Elephant(Animal): #single inheritance with overriding method sound()
    def sound(self):
        return "Triumph"


class Tiger(Lion): #multilevel inheritance.Acquires all attributes from Animal and Lion class
    pass

tiger=Tiger()
print("******Tiger******")
print(tiger.eat())
print(tiger.sound())
print(tiger.sleeps())

lion =Lion()
print("******Lion******")
print(lion.eat())
print(lion.sleeps())
print(lion.sound())

ele=Elephant()
print("******-Elephant*******")
print(ele.sleeps())
print(ele.eat())
print(ele.sound())