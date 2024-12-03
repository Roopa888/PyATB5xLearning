class A:
    def methodA(self):
        return ("Method A")


class B(A):
    def methodB(self):
        return ("Method B")


class C(A):
    def methodC(self):
        return ("Method C")


class D(B, C):              # eg:single inheritance (for B and C) and then multiple/multilevel inheritance for D --->hybrid
    def methodD(self):
        return ("Method D")

d=D()               #d can access all methods and attributes in all classes because it inherits from all classes
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())

