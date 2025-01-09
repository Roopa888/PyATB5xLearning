import time

from selenium import webdriver
import pytest
import allure

@allure.title("Open the app/vmo.com")
@pytest.mark.regression
def test_vmo_login():
    driver=webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    time.sleep(5)
