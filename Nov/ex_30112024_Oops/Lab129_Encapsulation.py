class VMOLoginpage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_Confirm(self):
        if self.email == "Roopa@gmail.com" and self.password == "Pass123":
            print("Login Successful")
        else:
            print("Login failed")


# email = input("Enter the email\n")
# password = input("Enter the password \n")
# vmo_obj = VMOLoginpage(email, password)
vmo_obj=VMOLoginpage("Roopa@gmail.com","Pass123")
vmo_obj.login_Confirm()
