# Find  element with  alan and edit the job status
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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
    # Path to find all elements (first & Middle name)->//div[@role='table']/div[2]/div[3]/div[1]/div[3]
    # can be divided as below
    # first_part="//div[@role='table']/div[2]/div["
    # 3-->This keeps changing as the row changes- 1 to 50 or so.Can use i here to get the dynamic path
    # second_part="]/div[1]/div[3]"
    first_part = part = "//div[@role='table']/div[2]/div["
    second_part = "]/div[1]/div[3]"  # last div[3] denotes the fistname in evry row

    no_of_rows = len(driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div"))
    for i in range(1, no_of_rows + 1):
        dynamic_path = f"{first_part}{i}{second_part}"
        data_element = driver.find_element(By.XPATH, dynamic_path)
        if "alan" in data_element.text:
            # //div[@role='table']/div[2]/div[3]/div[1]/div[3]/following-sibling::div[6]//button/i[contains(@class,'pencil-fill')]
            edit_icon_path = f"{dynamic_path}/following-sibling::div[6]//i[contains(@class,'pencil-fill')]"
            edit_icon = driver.find_element(By.XPATH, edit_icon_path)
            edit_icon.click()
            assert driver.current_url == "https://awesomeqa.com/hr/web/index.php/pim/viewPersonalDetails/empNumber/250"
            WebDriverWait(driver, timeout=4).until(
                EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Job']")))
            job_link = driver.find_element(By.XPATH, "//a[normalize-space()='Job']")
            job_link.click()
            time.sleep(4)
            emp_status = driver.find_element(By.XPATH,
                                             "//label[text()='Employment Status']/parent::div/following-sibling::div")
            # emp_status=driver.find_element("//div[@class='oxd-select-text-input' and normalize-space()='Working']")
            actions = ActionChains(driver=driver)
            actions.move_to_element(emp_status).click(on_element=emp_status).key_down(Keys.ARROW_DOWN).click().perform()
            # WebDriverWait(driver=driver, timeout=10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            time.sleep(5)
            save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            save_button.click()
            # actions.move_to_element(save_button).click(on_element=save_button).perform()
            print("Emp status after update")
            print(emp_status.text)
            time.sleep(10)
            # assert save_button.click()==True
            WebDriverWait(driver=driver, timeout=4).until(
                EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Employee List']")))
            emp_list = driver.find_element(By.XPATH, "//a[normalize-space()='Employee List']")
            emp_list.click()
            time.sleep(3)
            assert driver.current_url == "https://awesomeqa.com/hr/web/index.php/pim/viewEmployeeList"
            job_staus_update_xpath = f"{dynamic_path}/following-sibling::div[3]/div"
            print("Latest xpath", job_staus_update_xpath)
            job_staus_update_text = driver.find_element(By.XPATH, job_staus_update_xpath).text
            print(job_staus_update_text)
            assert job_staus_update_text == "Not Joined"
            print(driver.find_element(
                "//div[@role='table']/div[2]/div[3]/div[1]/div[3]/following-sibling::div[3]/div").text)
            print(f"Success-{data_element.text} has {job_staus_update_text}")
