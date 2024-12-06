class ExcelReader:
    @staticmethod
    def read_from_excel():
        print("Reading from Excel")
class MySQLDBConnection():
    @staticmethod
    def readMySQLFile():
        print("Reading My SQL file")

class TC1:
    static_var=10

    def testcase(self):
        MySQLDBConnection.readMySQLFile()
        ExcelReader.read_from_excel()
        print("Static variable",TC1.static_var) # shared among all instances of the class
tc1=TC1()
tc1.testcase()
#TC1.testcase() # to make this work you have to make it @staticmethod and remove self from argument list of testcase()