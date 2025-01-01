import pytest
import allure
import requests


@allure.title("Verify  the GET Request of teh Restful Booker ")
@allure.description("This testcase checks for the Booking1 and checks for the response")
@pytest.mark.positive
def test_get_request_positive():
    print("Testcase1")
    URL = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=URL)
    print(response_data.text)
    assert response_data.status_code == 200


@allure.title("Verify  the GET Request of the Restful Booker with invalid booking id ")
@allure.description("This testcase checks for the Booking1 with invalid ID and checks for the response")
@pytest.mark.negative
def test_get_request_negative():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    response_data2 = requests.get(url=URL)
    assert response_data2.status_code - -404
