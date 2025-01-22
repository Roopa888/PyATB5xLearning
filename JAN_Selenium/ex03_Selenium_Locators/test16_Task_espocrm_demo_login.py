import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
@allure.title("Espocrm login test case")
@allure.description("TC1-Positive TC-ESPOCRM login button click takes you to the next page")
@pytest.mark.postive
def test_espo_crm_login_chrome():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    login_web_element=driver.find_element(By.ID,"btn-login")
    login_web_element.click()
    time.sleep(3)
    assert driver.current_url=="https://demo.us.espocrm.com/?l=en_US"
    print("Login page displayed")
    time.sleep(2)
    driver.quit()