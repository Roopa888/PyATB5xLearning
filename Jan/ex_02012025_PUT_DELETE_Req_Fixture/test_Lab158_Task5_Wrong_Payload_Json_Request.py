# 5. Invalid Creation - enter a wrong payload or wrong JSON.
import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headerscom = {
    "Content-Type": "application/json"
}


def test_CreateBooking_Wrong_Payload():
    base_path_create = "/booking"
    create_Booking_url = base_url + base_path_create
    print(create_Booking_url)
    # The below Json has key name as "name" instead of "firstname" .It should throw error 500
    payload = {
        "name" : "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
    }
    response_create_Booking = requests.post(url=create_Booking_url, headers=headerscom, json=payload)
    response_create_Booking.status_code == 500
    response_create_Booking.text == "Internal Server Error"

