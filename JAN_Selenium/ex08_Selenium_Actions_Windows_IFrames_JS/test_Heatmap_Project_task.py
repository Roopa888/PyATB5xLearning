# Access the website which has two icon visble on hovering on it .
# Click and switch to child one of the icon  window that opens which has multiple iframes
# click on the "clickMap' icon" in one of those iframes
# Multiple concepts are being used here
import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

@allure.title("Windows_Iframe_Actions")
@allure.description("Verify Click Map in IFrame in the child window")
def test_multiple_concepts_hover_windows_iframe_click():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(
        "https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(),name="HeatMap Screehots-Initial page",attachment_type=AttachmentType.PNG)
    main_window= driver.current_window_handle  # 1
    print(main_window)
    # The below will get the 2 icons prsent --Control and Version as a list
    # control is list [0] ,version is list[1]
    list_two_web_elements = driver.find_elements(By.ID, "js-heatmap-thumbnail")
    variation = list_two_web_elements[1]
    actions = ActionChains(driver)
    actions.click(variation).perform()
    # WebDriverWait(driver=driver,timeout=20).until(EC.url_changes("https://courses.thetestingacademy.com/courses/job-ready-automation-tester-blueprint-with-java-by-pramod-dutta"))
    time.sleep(15)
    allure.attach(driver.get_screenshot_as_png(),name="HeatMap Screnshot-Second window-Step2",attachment_type=AttachmentType.PNG)
    window_handles_1 = driver.window_handles
    print(window_handles_1)



    for handle in window_handles_1:
        if handle != main_window:
            driver.switch_to.window(handle)
            print(handle)
            driver.switch_to.frame("heatmap-iframe") #iframe id is "heatmap-iframe"
            WebDriverWait(driver=driver,timeout=6).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,' vwo_player-option')]//span[text()='Clickmap']")))
            click_map=driver.find_element(By.XPATH,"//div[contains(@class,' vwo_player-option')]//span[text()='Clickmap']")
            click_map.click()
            time.sleep(10)
            allure.attach(driver.get_screenshot_as_png(), name="HeatMap Screnshot-Second window-Step2",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            print("Happy path")

    driver.quit()
