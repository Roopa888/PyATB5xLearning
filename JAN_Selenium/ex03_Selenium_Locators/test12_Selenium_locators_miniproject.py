# Log into app/vwo.com with a invalid username amd password
# Wait for 3 seconds and validate the error message
import time

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
@allure.title("VMO Login ngeative test case")
@allure.description("TC1-Negative TC-VWO login with negative creds")
@pytest.mark.negativevwologin
def test_app_vmo_login_chrome():
    load_dotenv()
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    # Find the email and enter the email in teh text field
    #< input
    #type = "email"
    #class ="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi" >
    email_web_element=driver.find_element(By.NAME,"username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))
    #Find the password locator and type the password
    #< input
    #type = "password"

    #class ="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe" >
    password_web_element=driver.find_element(By.ID,"login-password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))
    #<button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica">
    submit_btn_web_element=driver.find_element(By.ID,"js-login-btn")
    submit_btn_web_element.click()
    # wait for sometime
    time.sleep(3)
    # Get the error message text and print it
    #<div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    error_message_web_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text==os.getenv("error_message_expected")
    #driver.quit()