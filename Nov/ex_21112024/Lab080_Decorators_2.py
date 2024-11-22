# Second example

def add_before_UI_after_UI(func):
    def wrapper():
        print("Before running the UI test")
        print("Start the browser")
        func()
        print("After running the UI test ")
        print("Closing the browser")
    return wrapper()



@add_before_UI_after_UI
def test_UI():
    print(">>I am testing UI")