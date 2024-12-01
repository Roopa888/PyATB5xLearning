class Home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var = "child"

    def mom(self):
        print("Child :", self.__private_var)
        self.__wife()  #private function can be accessed from here

    def __wife(self):
        print("Wife")


obj_ref2 = Home()
# print(obj_ref2.__private_var) # cant access
#obj_ref2.__wife()  # cant access

print(obj_ref2.public_var)
print("*****")
obj_ref2.mom()
