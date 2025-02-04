import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("app.vwo.com login page with explicit waits")
@allure.description("Verify that app.vwo.com page is loaded with explicit waits")
def test_app_vwo_com_login_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_web_element = driver.find_element(By.CSS_SELECTOR, "input[id='login-username']")
    email_web_element.send_keys("abc@gmail.com")
    password_web_element = driver.find_element(By.CSS_SELECTOR, "input[id='login-password']")
    password_web_element.send_keys("1234")
    submit_button_web_element = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    submit_button_web_element.click()
    # Wait for the error message

    # A Condition to check the element
    # error_msg_element - comes after 2-4 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this

    # Smart Logic to wait for the element
    # Condition based Logic

    # Verify that message is visible.
    # if the webelement is found immediately the wait is ended and so execution time is less
    WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))

    # time.sleep(4) #Here python interpreter is halted for 5 seconds without any condition >less efficient
    error_message_web_element = driver.find_element(By.CSS_SELECTOR, "div[id='js-notification-box-msg']")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
