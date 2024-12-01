#Encapsulation means hiding the data members (instance variables) and will be exposed only by ts methods
class Car:
    model:None
    Name:None
    password:None # by default teh instance variables are public .We can make it private by "__"
    def __init__(self):
        self.password="Pass123"
        self.__password_secure="Wonder"



    def change_pass(self):
        print("Password is ", self.password)
        print("Secured password can be accessed from this function as this fn belongs to this class :",self.__password_secure)
obj_ref=Car()
print(obj_ref.password)
obj_ref.password="Geeta"
obj_ref.change_pass()
print(obj_ref.password)
#print(obj_ref.__password_secure)  #Error-Car' object has no attribute '__password_secure'. Did you mean: '_Car__password_secure'?