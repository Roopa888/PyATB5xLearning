from contextlib import nullcontext

import pytest
import allure
import requests


# pip install pytest allure requests
@allure.title("TC#1-Verify Create Booking -Positive")
@allure.description("Verify create booking !")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
    full_url = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # To send requests
    response_data = requests.post(url=full_url, headers=headers, json=payload)
    assert response_data.status_code == 200
    # Booking id >0
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    print(booking_id)
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    firstname = response_data_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str
    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True
    # https: // jsonpathfinder.com
    # x.booking.bookingdates.checkin
    # response_data_json["booking"]["bookingdates"]["checkin"]
    checkin = response_data_json["booking"]["bookingdates"]["checkin"]
    checkout = response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"
    time = response_data.elapsed.total_seconds()
    assert time < 3


@allure.title("TC#2-Verify the Create Booking-Negative")
@allure.description("Verify the create booking with invalid payload is not working")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path_post = "/booking"
    full_url1 = base_url + base_path_post
    headers = {
        "Content-Type": "application/json"
    }
    json_payload={}
    response_data2=requests.post(url=full_url1,headers=headers,json=json_payload)
    assert response_data2.status_code==500
    print(response_data2.text)
    assert response_data2.text=="Internal Server Error"

@allure.title("TC#3-Verify the Create Booking -Negative 2")
@allure.description("Verify the create booking with null value for firstname Not working")
@pytest.mark.crud
def  test_create_booking_nagtive_tc3():
    base_url="https://restful-booker.herokuapp.com"
    base_path_post="/booking"
    full_url2 = base_url + base_path_post
    headers={
        "Content-Type": "application/json"
    }

    json_payload2 = {
        "firstname": None,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data3=requests.post(url=full_url2,headers=headers,json=json_payload2)
    assert response_data3.status_code==500
    print(response_data3.text)
    assert response_data3.text=="Internal Server Error"
