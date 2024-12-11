# Using class
from Dec.ex_10122024_Modules.browserPackage.CloseBrowser import stop_Browser
from Dec.ex_10122024_Modules.browserPackage.OpenBrowser import start_Browser


class TestCase:
    def test_case(self):
        start_Browser()
        print("from a class ")
        stop_Browser()
obj_ref=TestCase()
obj_ref.test_case()