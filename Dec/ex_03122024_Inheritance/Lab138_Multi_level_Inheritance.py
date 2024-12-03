class GrandFather:
    def possession1(self):
        self.key1="1BHK"
        print("Grand father--->Alto")
        print("Key---",self.key1)
class Father(GrandFather):
    def possession2(self):
        self.key2="3BHK"
        print("Father----->SUV")
        print("Key----",self.key2)
class Son(Father):
    def possession3(self):
        self.key3="4BHK"
        print("Mother --->Dezire")
        print("Key---->",self.key3)

son2=Son()
son2.possession1()
father=Father()
GF=GrandFather()
print("From GF---",son2.key1)
GF.possession1()
father.possession1()
father.possession2()
print("*******************")
son2.possession2()
print("$$$$$$$$")
son2.possession3()
print(son2.key3)
print("$$$$$$$$")
GF.possession1()
#GF.possession3() # cant be accessed as the fn belongs to its child son
print(son2.key1)
print(son2.key2)