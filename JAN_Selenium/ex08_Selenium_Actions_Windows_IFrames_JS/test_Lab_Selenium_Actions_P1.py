import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Actions chains-P1")
@allure.description("Verify actions chains class functionality- for Keyboards")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "Panaroma").key_up(Keys.SHIFT).perform()
    time.sleep(10)
    driver.quit()
