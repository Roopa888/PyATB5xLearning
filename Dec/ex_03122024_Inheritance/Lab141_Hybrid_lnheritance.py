# multiple types of inheritance,
# such as single,
# multiple, and
# multilevel inheritance.
class GrandFather:
    def possession0(self):
        self.key0 = "1BHK"
        print("Grand father--->Alto")
        print("Key---", self.key0)


class Father(GrandFather):
    def possession1(self):
        self.key1 = "Bunglow"
        print("Father has SUV car")
        print(f"Also has a{self.key1}")


class Mother:
    def possession2(self):
        self.key2 = "2BHK"
        print("Mother has swift")
        print("Key --", self.key2)


class Brother(Father):
    def possession3(self):
        self.key3 = "3BHK"
        print("Brother has Ferrari")
        print("Also has ", self.key3)


class Uncle():
    def possession5(self):
        self.key5 = "Villa"
        print("Uncle has Ambassador")
        print("Also has ", self.key5)


class Sister(Brother,
             Mother):  # Here multiple inheritance is present .Again brother itself has mutilevel  inheritance-MRO(Method Resolution Order - FCFS
    def possession4(self):
        self.key4 = "Duplex House"
        print("Sister has a Tiago")
        print(f"Also has a {self.key4}")


father = Father()
mother = Mother()
bro = Brother()
sis = Sister()
sis.possession4()  # mutiple inheritance
print("***************")
sis.possession2()
print("***************")
sis.possession1()  # mutilevel inheritance
print("***************")
sis.possession0()
print("***************")
sis.possession3()
