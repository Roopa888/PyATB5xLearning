import pytest
@pytest.fixture()
def create_token():
    return "abc"


@pytest.fixture()
def create_booking_id():
    return 1
@pytest.fixture()
def read_from_excel():
    return "xyz"

def test_put_request(create_token, create_booking_id):
    print(create_token)
    print(create_booking_id)
def test_put_request_2(create_token, create_booking_id,read_from_excel):
    print(create_token)
    print(create_booking_id)
    print(read_from_excel)