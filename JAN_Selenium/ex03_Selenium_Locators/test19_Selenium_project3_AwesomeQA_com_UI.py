import pytest
import allure
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
@allure.title("Verify the registration functionaity of AWESOME QA site")
@allure.description("Verify that a registration can be done with the given details on te Awesome QA website")
def test_awesome_qa():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("AWESOMEQA_URL"))
    time.sleep(3)
    first_name_web_element = driver.find_element(By.CSS_SELECTOR, "input#input-firstname")
    first_name_web_element.send_keys(os.getenv("AWESOMEQA_first_name"))
    last_name_web_element = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    last_name_web_element.send_keys(os.getenv("AWESOMEQA_last_name"))
    email_web_element = driver.find_element(By.CSS_SELECTOR, "input#input-email")
    email_web_element.send_keys(os.getenv("AWESOMEQA_email"))
    telephone_web_element = driver.find_element(By.CSS_SELECTOR, "input[name='telephone']")
    telephone_web_element.send_keys(os.getenv("AWESOMEQA_phone"))
    password_web_element = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password_web_element.send_keys(os.getenv("AWESOMEQA_password"))
    confirm_password_web_element = driver.find_element(By.XPATH, "//input[@name='confirm']")
    confirm_password_web_element.send_keys(os.getenv("AWESOMEQA_Confpassword"))
    checkbox_web_element = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox_web_element.click()
    continue_button_web_element = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    continue_button_web_element.click()
    time.sleep(4)
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    text_to_be_checked = driver.find_element(By.XPATH,
                                             "//div[@id='content']//*[text()='Your Account Has Been Created!']")
    assert text_to_be_checked.is_displayed()
    print(driver.title)
