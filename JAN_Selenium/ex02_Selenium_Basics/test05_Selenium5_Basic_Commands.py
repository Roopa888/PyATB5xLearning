from selenium import webdriver
import allure
import pytest


def test_vmo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    print((driver.current_url))
    print(driver.page_source)
