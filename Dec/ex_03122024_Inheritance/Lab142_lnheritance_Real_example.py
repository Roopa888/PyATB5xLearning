class BaseTest:
    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from excel")

    def close_browser(self):
        print("Closing the browser")


class TestCase1(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Test case P1 executed")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N1 executed")
        self.read_from_excel()
        self.close_browser()


class TestCase2(BaseTest):
    def execute_test2(self):
        self.open_browser()
        print("Test case2 executed")
        self.read_from_excel()
        self.close_browser()


class TestCase3(BaseTest):
    def execute_test3(self):
        self.open_browser()
        print("Test case3 executed")
        self.read_from_excel()
        self.close_browser()
tc3=TestCase3()
tc3.execute_test3()
print("________________")
tc1=TestCase1()
tc1.test_negative()