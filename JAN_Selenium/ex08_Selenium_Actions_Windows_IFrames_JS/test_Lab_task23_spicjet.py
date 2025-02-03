import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType #For getting screenshots in the allure report import this




@allure.title("SpiceJet Booking Automation")
@allure.description("Verify spice jet automation by using Action class")
def test_spuce_jet_booking_actionchains():
    chrome_options=webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.geolocation": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://www.spicejet.com/")
    allure.attach(driver.get_screenshot_as_png(), name="Spice Jet Booking Automation-Initial", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    source_city=driver.find_element(By.XPATH,"//div[normalize-space()='From']//input[@class='css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu']")
    actions=ActionChains(driver=driver)
    actions.move_to_element(source_city).click(on_element=source_city).perform()
    #actions.send_keys("Del").perform()
    actions.send_keys("Del").key_down(Keys.ARROW_DOWN).perform()
    time.sleep(5)
    # As soon as the first element is typed the tab goes to the destination automatically ,so there is no need to hit tab after typing the source city .We can just type the destination like below
    actions.send_keys("Blr").key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    #destin_city=driver.find_element(By.XPATH,"//div[normalize-space()='To']//input[@type='text']")
    allure.attach(driver.get_screenshot_as_png(), name="Spice Jet booking trip Automation-Final", attachment_type=AttachmentType.PNG)
    time.sleep(10)
    #driver.quit()