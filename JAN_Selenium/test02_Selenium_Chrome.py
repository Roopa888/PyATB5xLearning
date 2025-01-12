from selenium import webdriver
import pytest
import allure
@allure.title("Open the app/vmo.com")
@pytest.mark.regression
def test_vmo_login_chrome():
    driver=webdriver.Chrome()
    #The below code will be translated to teh API request
    #It will be a POSt request to teh browser driver (server)
    # Where it will create a session or fresh copy of teh browserChrome)
    # Session ID will be created=16 digit
    driver.get("https://app.vwo.com/#/login")
    print(driver.session_id)
    #GET API request to navigate to the page
    #Browser will navigate to teh URL
    #Source code(Client)-->API Request(using W3C protocol)-->Browser Driver(server)--->Instructions to browser
    # session id-65e2071d0cecab6410b75d672a705eac