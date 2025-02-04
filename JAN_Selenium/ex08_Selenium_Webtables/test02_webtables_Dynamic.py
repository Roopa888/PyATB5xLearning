# To print all the elements in a web table kind of structure (not the real table) (Orange HRM site)
# Actually it is a div class but some knd of table structured
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username.send_keys("admin")
    password.send_keys("Hacker@4321")
    submit_button.click()
    time.sleep(5)
    assert driver.current_url == "https://awesomeqa.com/hr/web/index.php/pim/viewEmployeeList"
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
    for i in range(1, no_of_rows + 1):
        for j in range(1, no_of_cols + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Terminated" in data:
                element = f"{dynamic_path}/preceding-sibling::div[3]"
                print(element)
                element_text = driver.find_element(By.XPATH, element).text
                print(f"====={element_text}")
    driver.quit()
