# To write to a file we can use append function
#if the file does not exist a new fiel will be cretaed in teh current directory and content will be appended each time during the run
with open("Sample1.txt","a") as file:
    file.write("This is a sample file \n")
    file.close()