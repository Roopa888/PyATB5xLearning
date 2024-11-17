# Match statement is similar to Switch statement in Java
# Available in Python >3.10 version
# working--Match the op and execute
# Like multiple -> If else loops
# syntax
# match variable:
#   case pattern1:
#       code block
#   case pattern 2:
#         code block
# Write a program to ask teh user which browser he wants to run automation with
# use logic building method and write the code as below
# Note that the pattern is case-sensitive -"Firefox" and "firefox" are different if we give as i/p below
browser_name = input("Enter the browser name \n")
match browser_name:
    case "firefox":
        print("Starting firefox")
    case "edge":
        print("Execute the code in edge ")
    case "safari":
        print("Starting safari")
    case "chrome":
        print("Execute the code in chrome ")
    case _: #default
        print("Browser not found")
