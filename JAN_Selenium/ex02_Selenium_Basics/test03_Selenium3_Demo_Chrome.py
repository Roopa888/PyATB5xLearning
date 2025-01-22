from selenium import webdriver
import allure
import pytest
from selenium.webdriver.ie.service import Service
# For selenium 3 we have to explicitly downlaod webdriver for each browser
#Selenium 4 onwards the selenium manager will downlaod the webdriver for each browser automatically

def test_vmo_sample_selenium_3():
    driver_path='C:\\Users\\aslog\\Downloads\\edgedriver_win64\\msedgedriver.exe'
    driver=webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://www.msn.com/")