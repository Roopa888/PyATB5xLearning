class MathUtils:
    def add(self, a, b):
        return a + b

    def add(self,a,b=0,c=0,d=0):  # latest signature in function always takes precedence when functions with same name exists inside a  class
        return a + b + c+d         # You can acheieve overloading only by providing the def values as in this case,otherwise error


mu = MathUtils()
print(mu.add(1, 2))
print(mu.add(3, 4, 5))
print(mu.add(2, 3))
print(mu.add(1,7,8,10))
print(mu.add(2,4))
print(mu.add(2))
