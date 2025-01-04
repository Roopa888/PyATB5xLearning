# Task #2- Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headerscom = {"Content-Type": "application/json"}


# The below function is a normal function which will return a token automatically
def create_token1():
    base_path_create_token = "/auth"
    create_token_url = base_url + base_path_create_token
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response_data_create_token = requests.post(url=create_token_url, headers=headerscom, json=payload)
    assert response_data_create_token.status_code == 200
    response_data_create_token_json = response_data_create_token.json()
    token = response_data_create_token_json["token"]
    assert len(token) > 0
    return token


def test_create_booking():
    base_path_create_booking = "/booking"
    full_url = base_url + base_path_create_booking
    payload = {
        "firstname": "Kim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=full_url, headers=headerscom, json=payload)
    assert response_data.status_code == 200
    response_data_json = response_data.json()
    assert response_data_json["bookingid"] > 0
    booking_id = response_data_json["bookingid"]
    print(booking_id)
    assert response_data_json["booking"]["firstname"] == "Kim"
    assert response_data_json["booking"]["lastname"] == "Brown"
    assert response_data_json["booking"]["totalprice"] == 111
    assert response_data_json["booking"]["depositpaid"] == True
    assert response_data_json["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response_data_json["booking"]["bookingdates"]["checkout"] == "2019-01-01"
    assert response_data_json["booking"]["additionalneeds"] == "Breakfast"
    return booking_id


def test_Delete_Booking():
    booking_id_del = str(test_create_booking())
    print(booking_id_del)
    base_path_del = "/booking/" + str(booking_id_del)
    full_url_delete = base_url + base_path_del
    cookie = "token=" + create_token1()
    print(cookie)
    headers1 = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response_data_del = requests.delete(url=full_url_delete, headers=headers1)
    assert response_data_del.status_code == 201
    return booking_id_del


# The below calls Delete Booking which in turns call create and then teh create-->Delete and Get will be executed in sequence
def test_GET_Del():
    booking_id_final = str(test_Delete_Booking())
    base_path_url_del = "/booking/" + booking_id_final
    DELETEURL = base_url + base_path_url_del
    print(DELETEURL)
    cookie_get = "token=" + create_token1()
    print(cookie_get)
    headers2 = {
        "Content-Type": "application/json",
        "Cookie": cookie_get
    }
    response_data_del = requests.post(url=DELETEURL, headers=headers2)
    assert response_data_del.status_code == 404
    assert response_data_del.text == "Not Found"
