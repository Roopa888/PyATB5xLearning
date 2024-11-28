class Dog:
    name = None
    breed = None
    height = None
    weight = None
    race = None

    # parametrised constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Behavior

    def bark(self):
        print("Barking")

    def sleep2(self):
        print("Who is sleeping", self.name)

    def talk(self):
        pass


# Object reference
chow_ref = Dog("chow", "mastiff")  # called with default constructor
print(chow_ref.name)
print(chow_ref.breed)
print(chow_ref.height)
chow_ref.sleep2()
print(id(chow_ref))
# Another object reference
mow_ref = Dog("Mow", "Husky")
print(mow_ref.name)
mow_ref.bark()
print(id(mow_ref))