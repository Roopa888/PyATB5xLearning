from http.client import responses

import pytest
import allure
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    print("User name--->", username)
    print("Password---->", password)
    url_create = "https://restful-booker.herokuapp.com/auth"
    headers = {
        "Content-Type": "application/json"

    }
    payload = {
        "username": username,
        "password": password
    }
    response_data = requests.post(url=url_create, headers=headers, json=payload)
    token = response_data.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
    url_create_booking = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type": "application/json"
    }
    payload2 = {
        "firstname": "Simony",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=url_create_booking, headers=headers, json=payload2)
    assert response_data.status_code==200
    print(url_create_booking)
    print(headers)
    print(payload2)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id
@pytest.fixture()
def launch_browser():
    print("Launching the browser")
    return "Chrome"
@pytest.fixture()
def Close_browser():
    print("Closing the browser")
    return "Closed Chrome"


@pytest.fixture()
def read_csv_file_data():
    pass


@pytest.fixture()
def read_mysql_file_database():
    pass


@pytest.fixture()
def read_url_test_data_excel():
    pass
