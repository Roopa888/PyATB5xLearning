import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
@allure.title("Espocrm Sales pack test case")
@allure.description("TC3-Positive TC-ESPOCRM Sales pack link takes you to the respective page")
@pytest.mark.postive
def test_espo_sales_pack_chrome():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    load_dotenv()
    driver=webdriver.Chrome(chrome_options)
    driver.get(os.getenv("ESPOURL"))
    time.sleep(5)
    sales_pack_web_element=driver.find_element(By.LINK_TEXT,'Sales Pack')
    sales_pack_web_element.click()
    time.sleep(3)
    driver.quit()
