import pytest
import allure
import requests
def test_update_req1(create_token,create_booking_id):
    print("Token--->",create_token)
    print("Booking Id---->",create_booking_id)

# We can call teh conftest.py functions (fixture)in any functions
def test_update_req2(create_token,create_booking_id,read_csv_file_data):
    print("Token--->",create_token)
    print("Booking Id---->",create_booking_id)
def test_update_req3(create_token,create_booking_id):
    print("Token--->",create_token)
    print("Booking Id---->",create_booking_id)
def launch_browser():
    print("Launching the browser")
    return "Chrome"
def Close_browser():
    print("Closing the browser")
    return "Closed Chrome"