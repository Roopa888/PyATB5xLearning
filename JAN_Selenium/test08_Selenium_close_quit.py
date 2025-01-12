# close will only close teh current active winodw
#quit will quit the driver and closes all the associated windows
import time

from selenium import webdriver
import pytest
import allure
def test_katalon_firefox():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    #driver.close()
    driver.quit()

