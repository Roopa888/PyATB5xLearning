# The name need not be exactly main()
# Can have mutiple methids as main
def this_name_can_be_anything1():
    print("The main method name can be anything-Method1")
def this_name_can_be_anything2():
    print("The main methid name can be anything-Method2")
# All it looks for is the line "if __name=="
if __name__=="__main__":
    this_name_can_be_anything1()
    this_name_can_be_anything2()
