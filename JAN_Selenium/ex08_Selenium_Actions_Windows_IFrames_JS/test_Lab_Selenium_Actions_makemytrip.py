import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType  # For getting screen shots in the allure report import this


@allure.title("Make my trip Automation")
@allure.description("Verify make my trip automation by using Action class")
def test_make_my_trip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    WebDriverWait(driver=driver, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']")))
    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()
    time.sleep(5)
    # from_city=driver.find_element(By.XPATH,("//input[@placeholder='From']"))
    from_city = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver=driver)
    actions.move_to_element(from_city).click().perform()
    time.sleep(2)
    actions.send_keys("Che").perform()
    # from_city.send_keys("DEL")
    time.sleep(2)
    actions.move_to_element(from_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    allure.attach(driver.get_screenshot_as_png(), name="Make my trip Automation", attachment_type=AttachmentType.PNG)
    time.sleep(4)
    driver.quit()
