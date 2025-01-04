import pytest
import allure
import requests


def test_Selenium(launch_browser,Close_browser):
    launch_browser
    print("Do TC")
    Close_browser
