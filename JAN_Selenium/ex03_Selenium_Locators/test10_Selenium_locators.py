#### Automation the mini project
# 1. Navigate to the URL - [﻿katalon-demo-cura.herokuapp.com/](https://katalon-demo-cura.herokuapp.com/)
# 2. Find the button
# 3. Click on it
# 4. Verify that URL changes or new URL comes.
import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
@allure.title("Katalon cliking the link and verify that the URL changes")
def test_katalon_firelfox():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    #Find the element
    #<a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    # click on it
    make_appointment_element.click()
    # Verify that the URl changes
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()