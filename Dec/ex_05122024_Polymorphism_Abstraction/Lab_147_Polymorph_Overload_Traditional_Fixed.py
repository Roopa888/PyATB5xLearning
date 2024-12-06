#Actual method overloading is never supported in Python
class Calc:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):          # give a default value for c then hen this fucntion is called this will work with 2 arguments also
        return a+b+c

calc_ref=Calc()
calc_ref.sum(3,4)
result=calc_ref.sum(3,4)
print(result)