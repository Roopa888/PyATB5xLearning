import time

from selenium import webdriver
import pytest
import allure


@allure.title("Verify that the title and current url of the espocrm webpage are as expected")
def test_espocrm():
    driver = webdriver.Firefox()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(20)
    assert driver.title == "EspoCRM Demo"
    assert driver.current_url == "https://demo.us.espocrm.com/"
