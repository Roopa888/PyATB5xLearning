import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
@allure.title("Espocrm personal demo test case")
@allure.description("TC4-Positive TC-ESPOCRM personal demo link takes you to the respective page")
@pytest.mark.postive
def test_espo_personal_demo_pack_chrome():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    load_dotenv()
    driver=webdriver.Chrome(chrome_options)
    driver.get(os.getenv("ESPOURL"))
    time.sleep(5)
    personal_demo_web_element=driver.find_element(By.LINK_TEXT,"personal demo")
    personal_demo_web_element.click()
    time.sleep(4)
    assert driver.current_url=="https://www.espocrm.com/cloud-registration/?plan=demo"
    driver.quit()