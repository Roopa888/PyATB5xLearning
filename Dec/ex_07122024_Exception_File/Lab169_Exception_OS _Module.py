import os

print("The current working directory is :",os.getcwd())
 # List the directories
files=os.listdir("/Users/aslog/PycharmProjects/PyATB5xLearning/") # Hidden directories also will be shown in the list
print(f"Files in the directory: {files}")
files=os.listdir() #can use it blank or "." to list the current dir
print(f"Files in the directory: {files}")

# Create a new directory (default -it will create in CWD

#os.mkdir('Test2')

# check if afile exists
#file_exists=os.path.exists("C:/Users/aslog/PycharmProjects/PyATB5xLearning/Dec/ex_07122024_Exception_File/TestData.txt")
#file_exists=os.path.exists("TestData.txt")
file_exists=os.path.exists("TestData1.txt")

print(file_exists) #returns True or False