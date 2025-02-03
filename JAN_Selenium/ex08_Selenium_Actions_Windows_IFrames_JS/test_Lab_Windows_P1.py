import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
@allure.title("Windows example")
@allure.description("Winodws handler method")
def test_windows_handlers():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(3)
    parent_window=driver.current_window_handle #unique window handler id
    print(parent_window)
    link1=driver.find_element(By.LINK_TEXT,"Click Here")
    link1.click()
    window_handles1=driver.window_handles
    print(window_handles1) #now 2 tabs are there .So ahndles ID will be printed-->['7F441BBEB1CA21FDCED1F9281C9F3027', 'A32D50812A655E46209FEFA24E9466A7']
    for handle in window_handles1:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Test case passed-Swicted to New window")
            break
    time.sleep(5)
    driver.quit()