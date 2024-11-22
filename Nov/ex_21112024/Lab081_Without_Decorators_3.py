# Same example (Lab080)if we do without decorator
# 3functions

def start():
    print("Before running the UI test")
    print("Start the browser")


def end():
    print("After running the UI test ")
    print("Closing the browser")


def test_UI():
    print("I am testing UI")
start()
test_UI()
end()