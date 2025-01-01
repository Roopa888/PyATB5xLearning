import pytest
import allure
import requests
@allure.title("TC#1-Verify that 2-2 ==0")
@allure.description("The test is check the basic math function ")
@pytest.mark.smoke
def test_basic_math():
    assert 2-2==0
@allure.title("TC #2-Verify that 3-3==0")
@allure.description("This is a regression  test which checks for 3--3")
@pytest.mark.regression
def test_sub1():
    assert 3-3==0

@allure.title("TC#3-Verify that 1-1 ==0")
@allure.description("The test is check the basic math function-1-1 ")
@pytest.mark.smoke
def test_sub2():
    assert 1-1==0
@allure.title("TC#4-Verify that 0-0 ==0")
@allure.description("The test is check the basic math function-1-1 ")
@pytest.mark.skip(reason="Not working now")
def test_sub3():
    assert 0-0!=0