class Father:
    def possession1(self):
        self.key1="1BHK"
        print(f"Key--{self.key1}")
        print("car---Alto")
class Mother:
    def possession2(self):
        self.key2="2BK"
        print(f"Key---->{self.key2}")
class Son(Mother,Father):
    def possession3(self):
        self.key3="3BHK"
        print(f"key---->{self.key3}")
son1=Son()
son1.possession2()
son1.possession3()
print("Variable from function 2",son1.key2)
print("Variable from own function ",son1.key3)
son1.possession1()
print(son1.key1)