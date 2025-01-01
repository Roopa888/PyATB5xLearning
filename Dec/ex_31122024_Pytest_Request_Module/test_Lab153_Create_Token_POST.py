import pytest
import allure
import requests
#Create Token -POST
#pipinstall pytest allure requests
base_url = "https://restful-booker.herokuapp.com"
headers={
    "Content_Type":"application/json"
}

def test_create_token_positive():
    base_path_post = "/auth"
    full_url4 = base_url + base_path_post
    payload={
    "username" : "admin",
    "password" : "password123"
    }
    response_data4=requests.post(url=full_url4,headers=headers,json=payload)
    print(response_data4)
    assert response_data4.status_code==200
    response_data_json4=response_data4.json()
    token=response_data_json4["token"]
    print(token)
    assert type(token)==str
    assert len(token)>0