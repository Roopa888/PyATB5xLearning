class Father:

    def possession1(self):
        self.key1 = "1BHK"
        print("Father --Car--->Audi")


class Mother:
    def __init__(self):
        print("DC - Mother")

    def possession1(self):
        self.key2 = "2BHK"
        print("Mother---Car--->Defender")


class Son(Mother, Father):

    def __init__(self):
        print("DC - Child")

    def possession2(self):
        self.key3 = "4BHK"
        print("Son--->Ferrari")
        print("Mother key-->", self.key2)


son3 = Son()
son3.possession1()  # possession1() is present for Father and Mother class ,but the one in mother class is calledd in inheritance order
print("*****")
son3.possession1()
son3.possession2()
