from browserPackage.OpenBrowser import start_Browser
from browserPackage.CloseBrowser import stop_Browser
# if we want without function
# start_Browser()
# print("TC is executing")
# stop_Browser()

# with function

def test_Case():
    start_Browser()
    print("TC is executing from the function")
    stop_Browser()


test_Case()
