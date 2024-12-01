class Person:
    def __init__(self,name):
      self.name=name

    def walk(self):
        return self.name

Ahan=Person("Ahan")
Preethi=Person("Preethi")
print(Ahan.name)
print(Preethi.name)
print("Who is walking" ,Preethi.walk())
print("Who is walking" ,Ahan.walk())



