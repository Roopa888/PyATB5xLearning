# for this testcase in the class recrding there was seen an issue for generating report at first and was advised to import Pytest
# and use decorator @pyetst.mark.smoke (still it was solved)/later had to restart Pycharm and run teh html report command
# But for my test case just teh belwo worked (w/0 pytest import) for the first time .Please note this point when refering this tc
import pytest


def method1():
    print("Hello World")


# To make it a Pytest testcase we have to mark it with test_
@pytest.mark.smoke  # just marked as it is a good practice
def test_method2():
    print("Testcase1")
    assert 1 - 1 == 2
@pytest.mark.regression
def test_method3():
    print("Testcase3")
    assert 1 + 1 == 2
