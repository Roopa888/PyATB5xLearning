# instance variable -within the class
# The value will get printed even if object is not instantiated
# The value will not get printed  if object is not instantiated.And also
# the obj_ref.print_info will give error 'Person' object has no attribute 'c' if print(self.c) is used
# for local variable (local to that function we don't need self ,just call them directly->print(c)
# we need self for instance variable
# local variable-within the function.# The value will not get printed  if object is not instantiated.And also
# the obj_ref.print_info will give error 'Person' object has no attribute 'c' if print(self.c) is used
# for local variable (local to that function we don't need self ,just call them directly->print(c)
# we need self for instance variable
a = 10  # global variable-can be accessed from anywhere
class Person:  # instance variable -within the class
    b = 11
    def print_info(self, gloabal=None):
        c = 12  # local variable-within the function
        print(c)
        print(self.b)
        global a
        a = "Hello"
        print("a inside function", a)
print(a)
object_ref = Person()
object_ref.print_info()
print("Outside",a)  # since we used global a and changed the value ,it rpints Hello .if we just use a="Hello" w/o dec gloabal keyword ,it will print 10
