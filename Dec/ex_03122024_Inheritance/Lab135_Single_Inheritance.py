class father:
    def print_info(self):
        print("Car-Alto")
        self.key1 = "2BHK"


class son(father):

    def print_info1(self):
        print("Car-SUV")
        self.key2 = "3BHK"


Father = father()
son1 = son()
#print(son1.key2)

son1.print_info()

son1.print_info1()
print(son1.key2)
Father.print_info()
print(Father.key1)
