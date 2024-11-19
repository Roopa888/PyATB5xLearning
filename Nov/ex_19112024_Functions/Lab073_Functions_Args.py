# Functions iwth multiple arguments
#*args means ---> a list of arguments we give as arguements (a tuple)
# We can iterate through it using a  For loop
# We can give any number of arguments here--->unlimited number of arguments

def multiple_arguments(* args):
    print(args)
    for i in args:
            print(i)
multiple_arguments("Olga")
multiple_arguments("Mariot","Jill","Helen","Savitha")
multiple_arguments("Kanika","Payal")
# arguments can be of any data type also
multiple_arguments("Jack",45,True)