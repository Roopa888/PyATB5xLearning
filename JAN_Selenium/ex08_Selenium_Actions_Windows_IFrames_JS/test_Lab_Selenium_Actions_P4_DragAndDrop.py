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
from allure_commons.types import AttachmentType


@allure.title("Action Class-Draggable")
@allure.description("Verify that an element can be dragged")
def test_verify_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.ID, "draggable")))
    element_to_hold = driver.find_element(By.ID, "draggable")
    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=element_to_hold).perform()
    time.sleep(10)
    element_where_to_drop = driver.find_element(By.ID, "droppable")
    actions.drag_and_drop(source=element_to_hold, target=element_where_to_drop).perform()
    allure.attach(driver.get_screenshot_as_png(), name="Awesome QA mouse interaction page-Drag and drop",
                  attachment_type=AttachmentType.PNG)
    time.sleep(4)
