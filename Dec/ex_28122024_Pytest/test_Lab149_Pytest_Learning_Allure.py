import pytest
import allure
@allure.title("Verify that the test case  with valid data is working")
@allure.description("This testcase checks for the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("Testcase1")
    assert 1 - 1 == 2


# To make it a Pytest testcase we have to mark it with test_
@allure.title("Verify that the test case  with invalid data is working")
@allure.description("This testcase checks for the negative create booking")
@pytest.mark.negative  # just marked as it is a good practice
def test_create_booking_negative1():
    print("Testcase1")
    assert 1 + 1 == 2


@allure.title("Verify that the test case  with invalid data is working")
@allure.description("This testcase checks for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative2():
    print("Testcase3")
    assert 1 + 1 == 2
