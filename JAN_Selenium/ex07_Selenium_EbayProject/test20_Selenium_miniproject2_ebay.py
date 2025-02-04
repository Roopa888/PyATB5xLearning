# Open the Url - ﻿www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get al the prices
# Print all the titles and prices in the end.

import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Verify the search function of the ebay .com page with macmini in search page-Should return 62 items ")
@allure.description(
    "TC1-Postive test case-Search for macmini computers in the search box of Ebay.com page and print the titles and prices of all listed items")
def test_ebay_com_page_Chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(2)
    # //input[@title="Search"]
    search_input_web_element = driver.find_element(By.XPATH, "//input[@title='Search']")
    search_input_web_element.send_keys("Macmini")
    search_button_web_element = driver.find_element(By.XPATH, "//span[text()='Search']")
    search_button_web_element.click()
    list_macmini_titles = driver.find_elements(By.CSS_SELECTOR, "div.s-item__title")
    # just with dot also CSS selector can locate the element as shwon below
    # list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    # price-CSS selector-->span.s-item__price
    list_macmini_prices = driver.find_elements(By.CSS_SELECTOR, "span.s-item__price")
    print("Macmini computers listed with proces  are:")
    print(len(list_macmini_titles))
    # Two lists are combined using zip function and converted to list and printed the titel and prices
    for items, items_price in (list(zip(list_macmini_titles, list_macmini_prices))):
        print(items.text)
        print(items_price.text)

    time.sleep(4)
    driver.quit()
