from selenium import webdriver
import allure
import pytest
@allure.title("Verify that the title for VMO login page is as expected ")
def test_vmo_sample():
    driver=webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    assert driver.title=="Login - VWO"