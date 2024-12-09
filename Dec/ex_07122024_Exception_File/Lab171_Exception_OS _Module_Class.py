class XYZ:
    def f1(self):
        try:
            num1 = int((input("Enter the value for num1\n")))

        except Exception as e:
            print("Enter only integer value for num1")
        else:
            print("The num is ", num1)
        finally:
            print("FINALLY:This block will be executed anyhow")
xyz_ref=XYZ()
xyz_ref.f1()