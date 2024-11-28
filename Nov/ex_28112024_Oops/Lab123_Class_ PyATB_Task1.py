# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
# Use PC - to set the value of the attributes
# create a Print student information method/function
# 3 students objects
# PyATB().print_student_information()
class PyATB:
    name = None
    regnum = None
    batchname = None
    role = None
    experience_years = None

    def __init__(self, name, regnum, batchname, role, experience_years):
        self.name = name
        self.regnum = regnum
        self.batchname = batchname
        self.role = role
        self.experience_years = experience_years

    def print_student_information(self):
       print(f"PyATB Student name is :{self.name}\n",f"PyATB Student registration num is :{self.regnum}\n",f"PyATB Student batch name is :{self.batchname}\n",f"PyATB Student role is :{self.role}\n",f"PyATB Student experience(years) is :{self.experience_years}\n")
       # for i in range(3):
#
#     name1 = input("Enter the name of PyATB student:\n")
#     regnum1 = input("Enter the reg number of PyATB student:\n")
#     batchname1 = input("Enter the batch name of PyATB student:\n")
#     role1 = input("Enter the role of PyATB student:\n")
#     experience_years1 = input("Enter the experience(years) of PyATB student:\n")
#     student1 = PyATB(name1, regnum1, batchname1, role1, experience_years1)
# #print("The student information of 3 student objects are as below\n")
#     student1.print_student_information()
student1=PyATB("Hema","1001","5ATB","Manual tester","5")
student2=PyATB("Prathiba","1002","5ATB","Fresher","1")
student3=PyATB("Rohan","1003","6ATB","SDET","7")
print("The student information of 3 PyATB students are as below\n")
student1.print_student_information()
student2.print_student_information()
student3.print_student_information()