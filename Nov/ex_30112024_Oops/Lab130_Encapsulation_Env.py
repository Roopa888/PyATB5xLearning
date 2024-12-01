from dotenv import load_dotenv
import os
class VMOLOginPage:
    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirm(self):
        if self.email=="Roopa@gmail.com" and self.password=="Pass@123":
            print("Login successful")
        else:
            print("Login Failed")

    # In future we will take the input email  from test data file --->Excel.csv or Env file
load_dotenv()
email=os.getenv("email")     # key name we can give "EMAIL" or "email".not case-sensitive
password=os.getenv("password")
print("email: "+email)
print("password: "+password)
vmj_obj2=VMOLOginPage(email,password)
vmj_obj2.login_confirm()