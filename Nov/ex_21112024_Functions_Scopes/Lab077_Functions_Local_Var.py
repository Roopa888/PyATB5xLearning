public_toilet="PT"
def home():
    print("Inside home")
    private_toilet="PR_T"
    print(private_toilet)
    public_toilet = "LPT"  #local variable value has the preference over gloabal inside a function
    print(public_toilet)
home()