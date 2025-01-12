import time

from selenium import webdriver
import allure
import pytest


@allure.title("Verify the current url of the katalon webpage is as expected ")
def  test_katalon_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
def test_katalon_edge():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
def test_katalon_firefox():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"