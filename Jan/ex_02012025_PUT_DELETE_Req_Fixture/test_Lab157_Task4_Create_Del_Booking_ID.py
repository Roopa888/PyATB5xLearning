# 4. Create a BOOKING, Delete It
import pytest
import allure
import requests
base_url = "https://restful-booker.herokuapp.com"
headerscom = {
    "Content-Type": "application/json"
}


def get_token():
    base_path_auth = "/auth"
    full_url = base_url + base_path_auth
    headers1 = {
        "Content-Type": "application/json"
    }
    payload1 = {
        "username": "admin",
        "password": "password123"
    }
    response_data_get_token = requests.post(url=full_url, headers=headers1, json=payload1)
    assert response_data_get_token.status_code == 200
    token = response_data_get_token.json()["token"]
    assert len(token) > 0
    return token


def create_Booking():
    base_path_create = "/booking"
    full_url = base_url + base_path_create
    headers_create = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "firstname": "Kathy",
        "lastname": "Woe",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_create = requests.post(url=full_url, headers=headers_create, json=payload)
    assert response_create.status_code == 200
    response_create_json = response_create.json()
    assert response_create_json["bookingid"] > 0
    booking_id = response_create_json["bookingid"]
    print(booking_id)
    assert response_create_json["booking"]["firstname"] == "Kathy"
    assert response_create_json["booking"]["lastname"] == "Woe"
    assert response_create_json["booking"]["totalprice"] == 111
    assert response_create_json["booking"]["depositpaid"] == True
    assert response_create_json["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response_create_json["booking"]["bookingdates"]["checkout"] == "2019-01-01"
    assert response_create_json["booking"]["additionalneeds"] == "Breakfast"
    return booking_id


def test_del_booking():
    del_booking_id = str(create_Booking())
    del_base_path = "/booking/" + del_booking_id
    final_url = base_url + del_base_path
    print(final_url)
    cookie = "token=" + get_token()
    headers1 = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    print(cookie)
    response_del = requests.delete(url=final_url, headers=headers1)
    assert response_del.status_code == 201
    search_del_url = base_url + "/booking/" + del_booking_id
    headers2 = {
        "Accept": "application/json"
    }
    response_get_data = requests.get(url=search_del_url, headers=headers2)
    print("*************Search after Delete-Updates response*****")
    assert response_get_data.status_code == 404
    assert response_get_data.text == "Not Found"
