
#button[onclick="jsAlert()"]
import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("JS Alerts")
@allure.description("Verify the 3 types of JS  alerts ")
def test_alerts_js_alerts_normal():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_js_alert=driver.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']")
    element_js_alert.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    alert_click_text=driver.find_element(By.ID,"result").text
    assert alert_click_text=="You successfully clicked an alert"
    time.sleep(4)
    #driver.quit()
def test_alerts_js_confirm():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_js_confirm_alert=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    element_js_confirm_alert.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.dismiss()
    alert_dismiss_text=driver.find_element(By.ID,"result").text
    assert alert_dismiss_text=="You clicked: Cancel"

def test_alerts_prompt():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_js_prompt_alert=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    element_js_prompt_alert.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.send_keys("Success")
    alert.accept()
    alert_prompt_text=driver.find_element(By.ID,"result").text
    assert alert_prompt_text=="You entered: Success"
    time.sleep(3)
    driver.quit()