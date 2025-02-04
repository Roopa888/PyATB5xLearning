from selenium import webdriver
import allure
import pytest


def test_katalon_demo_cura():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "PURA Healthcare Service" in driver.page_source:
        print("Text found!!..Test case passed")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found ", False)

# python interpreter is closing the browser
