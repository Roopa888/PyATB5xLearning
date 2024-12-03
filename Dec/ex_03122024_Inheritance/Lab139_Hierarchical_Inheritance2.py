class Father:
    def possession1(self):
        self.key1 = "3BHK"
        print("Father --->SUV")
        print("Key--", self.key1)


class Son(Father):
    def possession2(self):
        print("Son---Dezire")
        self.key2 = "Flat"
        print("Brother---->", self.key2)


class Daughter(Father):
    def possession3(self):
        self.key3 = "Studio Apartment"
        print("Sister ---Nano")
        print("From father  --", self.key1)


class Son2(Father):
    def possession1(self):
        print("Son2--->Bike")
        self.key4 = "1BHK"
        print("Key---->", self.key4)

    def possession4(self):
        print("Son2--->Yatch")
        self.gold = "1KG Gold"
        print("Key---->", self.gold)


son1 = Son()
son1.possession1()
print("***************")
son2 = Son2()
son2.possession1()  # Local member function gets preference if possession1() is present in both parent and child class
print("Key4--", son2.key4)
son2.possession4()
print("***************")
Dau = Daughter()
Dau.possession1()
#Dau.possession2() # Error-'Daughter' object has no attribute 'possession2'.