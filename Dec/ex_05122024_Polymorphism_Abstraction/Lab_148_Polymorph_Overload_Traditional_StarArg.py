# Method overloading using starta args
class Calc:
    def print_num(self,*args):
        for i in  args:
            print(i,end=" ")

class_ref=Calc()
class_ref.print_num(1)
print("\n***************")
class_ref.print_num(2,3)
print("\n***************")
class_ref.print_num(2,3,5)