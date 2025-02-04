import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options


@allure.title("Espocrm Advanced pack test case")
@allure.description("TC2-Positive TC-ESPOCRM Advanced pack link takes you to the respective page")
@pytest.mark.postive
def test_espo_advanced_pack_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    load_dotenv()
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("ESPOURL"))
    time.sleep(5)
    advanced_pack_link_web_element = driver.find_element(By.LINK_TEXT, "Advanced Pack")
    advanced_pack_link_web_element.click()
    time.sleep(15)
    assert driver.find_element(By.LINK_TEXT, "Advanced Pack").is_displayed()
    print("Advanced pack found")
    time.sleep(4)
    driver.quit()
