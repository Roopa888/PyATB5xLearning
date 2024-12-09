import os

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_filename = full_path + r"\example.txt"
    print(full_path_filename)
    file = open(full_path_filename)
    print(os.name)

# read a file
except  Exception as fnfe:
    print("File not found....")
     # FileNotFoundError: [Errno 2] No such file or directory: because file is not created.So we will try.. ..except this
finally:
    print("This will get executed anyhow") # it is generally expected to clos eteh file stream in any case.But Pythin will anyhow do it .So we did a print here
