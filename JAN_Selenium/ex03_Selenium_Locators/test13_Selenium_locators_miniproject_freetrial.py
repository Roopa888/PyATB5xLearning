#Click on teh free trail link onthe app.vmo login page
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
def test_app_vmo_login_all_links_chrome():
    load_dotenv()
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    #<a href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage" class="text-link" data-qa="bericafeqo">Start a free trial</a>
    # use the Link text and Partial text method of a tag (only availabel for a tag
    #Link text --->Exzct match
    # anchor_tag_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    # anchor_tag_element.click()
    anchor_tag_element=driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    anchor_tag_element.click()
    time.sleep(10)
    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    # driver.quit()
