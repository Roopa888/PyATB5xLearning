

import pytest
import allure
import requests

# Create Token -POST
# pipinstall pytest allure requests
base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}


# The below function is a normal function which will return a token automatically
def get_token():
    base_path_post = "/auth"
    full_url4 = base_url + base_path_post
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response_data_4 = requests.post(url=full_url4, headers=headers, json=payload)
    assert response_data_4.status_code == 200
    response_data_json4 = response_data_4.json()
    token = response_data_json4["token"]
    print(token)
    assert type(token)
    assert len(token) > 0
    return token


def get_booking_id():
    base_path = "/booking"
    full_url5 = base_url + base_path
    print(full_url5)
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
    response_data5 = requests.post(url=full_url5, headers=headers, json=payload)
    response_data5_json = response_data5.json()
    booking_id = response_data5_json["bookingid"]
    return booking_id


# The put request needs both token and booking id to operate
def test_put_request():
    token = get_token()
    booking_id = get_booking_id()
    print(token)
    print(booking_id)
    base_path_put="/booking/"+str(booking_id)
    full_url_put=base_url+base_path_put
    print(full_url_put)
    cookie = "token=" + token
    headers={
        "Content-Type":"application/json",
        "Cookie":cookie

    }
    payload={
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data_5=requests.put(url=full_url_put,headers=headers,json=payload)
    assert response_data_5.status_code==200
    assert response_data_5.json()["firstname"]=="Pramod"
def test_delete():
    URL="https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    DELETEURL=URL+str(booking_id)
    cookie_value="token="+get_token()
    headers={
        "Content-Type":"application/json",
        "Cookie":cookie_value
    }
    response_data=requests.delete(url=DELETEURL,headers=headers)
    assert response_data.status_code==201
