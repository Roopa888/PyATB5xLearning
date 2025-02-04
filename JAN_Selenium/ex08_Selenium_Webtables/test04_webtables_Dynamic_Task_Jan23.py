# https://awesomeqa.com/hr/web/index.php/auth/login
#
# username : admin
# Password : Hacker@4321
#
# Find the first element in the Webtable which is Terminated and click on the delete button
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_terminated_Delete():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    time.sleep(5)
    user_name = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    user_name.send_keys("admin")
    password.send_keys("Hacker@4321")
    submit_button.click()
    time.sleep(6)
    # WebDriverWait(driver=driver, timeout=10).until(EC.url_changes("https://awesomeqa.com/hr/web/index.php/pim/viewEmployeeList"))
    # The concept remains same as we used in static table .We need to identify the parts of xpath that changes and do not change
    # The individual elements can be accessed using --->//div[@role='table']/div[2]/div[7]/div[1]/div[3]
    # This can be further divided into as below

    # first_part="//div[@role='table']/div[2]/div["
    # 1to 7 --->row changes(actually more elments are there .but for the time being, we will consider these
    # second_part--->"]/div[1]/div["
    # 3---1 to 9
    # third_part--->"]"
    first_part = "//div[@role='table']/div[2]/div["
    second_part = "]/div[1]/div["
    third_part = "]"
    # use for loop to print individual elements
    no_of_rows = len(driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div"))
    no_of_cols = len(driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div[3]/div[1]/div"))
    for row in range(1, no_of_rows + 1):
        for col in range(1, no_of_cols + 1):
            dynamic_path = f"{first_part}{row}{second_part}{col}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            # Delete icon -->//div[@role='table']/div[2]/div[3]/div[1]/div[3]/following-sibling::div[6]//button/i[contains(@class,'bi-trash')]
            if "Terminated" in data:
                delete_icon_path = f"{dynamic_path}/following-sibling::div[3]//button/i[contains(@class,'bi-trash')]"
                print(delete_icon_path)
                delete_icon = driver.find_element(By.XPATH, delete_icon_path)
                print(f"The first employee terminated is {data}")
                print(delete_icon_path)
                delete_icon.click()
                WebDriverWait(driver=driver, timeout=2).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.orangehrm-modal-footer")))
                del_modal = driver.find_element(By.CSS_SELECTOR, "div.orangehrm-modal-footer")
                assert del_modal.is_displayed()
                allure.attach(driver.get_screenshot_as_png(), name="Orange HRM-Terminated -Delete--screenshot",
                              attachment_type=AttachmentType.PNG)
                time.sleep(10)
                break

        break

    driver.quit()
