public_toilet="PT"
def home():
    print("Inside home")
    private_toilet="PR_T"
    print(private_toilet)
    print(public_toilet)

def stranger():
    print("Stranger")
    print(public_toilet)
  #  print(private_toilet) # cant access this variable .Error=private_toilet' is not defined
home()
stranger()
# Accessing outside of all functions
#Only global variables can be accessed
print("Outside ")
print(public_toilet)
##print(private_toilet) #not defined error
