import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Actions chains-P1")
@allure.description("Verify actions chains class functionality- for Keyboards(Mouse)")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(3)
    results_page = driver.find_element(By.ID, "click")
    results_page.click()
    time.sleep(2)
    actions_builders = ActionBuilder(driver=driver)
    actions_builders.pointer_action.pointer_up(MouseButton.BACK)
    actions_builders.perform()
    time.sleep(10)
    driver.quit()
