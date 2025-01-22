import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
@allure.title("Verify the Options in webdriver")
def test_chrome_options():
    chrome_options= Options()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--window-size=400,600")
    chrome_options.add_argument("--headless")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)


