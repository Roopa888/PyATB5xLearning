#Create a file and write in it
import os

os.chdir(r"C:\Users\aslog\OneDrive\Desktop") # This will create
file_name = "Welcome1.txt"
content1 = "This is a file created via Program Lab172"
with open(file_name, "w") as file: # if file is not present it will create teh file and add teh content
    file.write(content1)

# Read  the file
with open(file_name,"r") as file:
    content2=file.read()
    print("The content of the file is ***:",content2)
    file.close()
    os.remove(file_name)
