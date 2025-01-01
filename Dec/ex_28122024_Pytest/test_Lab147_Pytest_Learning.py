def method1():
    print("Hello World")


# To make it a Pytest testcase we have to mark it with test_
def test_method2():
    print("This is a Pytest testcase")
    assert 5 == 5
