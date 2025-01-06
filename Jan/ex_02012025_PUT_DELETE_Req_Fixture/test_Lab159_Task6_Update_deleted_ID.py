# 6. Trying to Update on a Delete ID -> 404
import pytest
import allure
import requests
base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content=Type": "application/json"

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


def create_delete_Booking():
    base_path_create = "/booking"
    full_url = base_url + base_path_create
    headers_create = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "firstname": "Karoly",
        "lastname": "Watson",
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
    assert response_create_json["booking"]["firstname"] == "Karoly"
    assert response_create_json["booking"]["lastname"] == "Watson"
    assert response_create_json["booking"]["totalprice"] == 111
    assert response_create_json["booking"]["depositpaid"] == True
    assert response_create_json["booking"]["bookingdates"]["checkin"] == "2018-01-01"
    assert response_create_json["booking"]["bookingdates"]["checkout"] == "2019-01-01"
    assert response_create_json["booking"]["additionalneeds"] == "Breakfast"
    del_path = "/booking/" + str(booking_id)
    del_url = base_url + del_path
    cookie = "token=" + str(get_token())
    headers_del = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response_del_data = requests.delete(url=del_url, headers=headers_del)
    assert response_del_data.status_code == 201
    return booking_id


def test_update_del_booking_id(): #patch request
    update_path = "/booking/" + str(create_delete_Booking())
    update_url = base_url + update_path
    print(update_url)
    cookie = "token=" + str(get_token())
    print(cookie)
    headers_update = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    payload2 = {
        "firstname": "Nora",
        "lastname": "Jim"
    }
    response_patch_data = requests.patch(url=update_url, headers=headers_update, json=payload2)
    assert response_patch_data.status_code == 405
    assert response_patch_data.text == "Method Not Allowed"
