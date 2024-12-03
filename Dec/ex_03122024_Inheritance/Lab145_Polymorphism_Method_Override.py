#Method overriding occurs when a subclass provides a specific implementation of a method
# that is already defined in its superclass. This allows the subclass to customize or
# completely replace the behavior of the method inherited from the superclass
class Father:
    def home(self):
        print("4BHK")
class Son(Father):
    def home(self):
        print("2BHK")
        super().home()
        Father().home()
son3=Son()
father=Father()
print("++++++++++++++++++++++++++")
son3.home()
print("__________________________")
father.home()                   #The objects call that specific member function of that class they belong to