# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headerscom = {"Content-Type": "application/json"}


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


def Get_All_bookings_ID():
    booking_path = "/booking/"
    getAll_url = base_url + booking_path
    response_data1 = requests.get(url=getAll_url, headers=headerscom)
    response_data1_json = response_data1.json()
    print(response_data1_json)
    return (response_data1_json[0]["bookingid"])


def update_booking():
    update_booking_id = str(Get_All_bookings_ID())
    print("The booking id is", update_booking_id)
    update_path = "/booking/" + update_booking_id
    patch_url = base_url + update_path
    print(patch_url)
    cookie = "token=" + str(get_token())
    print("Welcome")
    print(cookie)
    headers2 = {"Content-Type": "application/json",
                "Cookie": cookie

                }
    payload2 = {
        "firstname": "Nora",
        "lastname": "Jim"
    }
    response_patch_data = requests.patch(url=patch_url, headers=headers2, json=payload2)
    # def test_Get_By_ID():
    #     update_Booking_ID = str(Update
    #     function)
    response_patch_data_json = response_patch_data.json()
    print("*************Updates response*****")
    assert response_patch_data.status_code == 200
    print(response_patch_data_json)
    assert response_patch_data_json["firstname"] == "Nora"
    assert response_patch_data_json["lastname"] == "Jim"
    print(response_patch_data_json["firstname"])
    print(response_patch_data_json["lastname"])
    return update_booking_id


def test_get_booking_by_id():
    booking_id = update_booking()
    base_path_get_booking = "/booking/" + booking_id
    final_url = base_url + base_path_get_booking
    headers3 = {
        "Accept": "application/json"
    }
    response_get_data = requests.get(url=final_url, headers=headers3)
    assert response_get_data.status_code == 200
    response_get_data_json = response_get_data.json()
    print("*************GET-Updates response*****")
    print(response_get_data_json)
    assert response_get_data_json["firstname"] == "Nora"
    assert response_get_data_json["lastname"] == "Jim"
    assert response_get_data_json["totalprice"] == 111
    assert response_get_data_json["depositpaid"] == True
    assert response_get_data_json["bookingdates"]["checkin"] == "2018-01-01"
    assert response_get_data_json["bookingdates"]["checkout"] == "2019-01-01"
   # assert response_get_data_json["additionalneeds"] == "Breakfast"
