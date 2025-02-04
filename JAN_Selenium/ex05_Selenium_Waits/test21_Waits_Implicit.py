import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("VWO login Page with waits")
@allure.description("TC1-Negative-Verify that VWO login page is loaded with waits")
@pytest.mark.negative
def test_app_vwo_com_implicit_waits():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.implicitly_wait(5)  # very rarely used -applicable to 0.01 %
    # input[id='login-username']
    # input[id='login-password']
    email_web_element = driver.find_element(By.CSS_SELECTOR, "input[id='login-username']")
    email_web_element.send_keys("abc@gmail.com")
    password_web_element = driver.find_element(By.CSS_SELECTOR, "input[id='login-password']")
    password_web_element.send_keys("1234")
    driver.quit()
