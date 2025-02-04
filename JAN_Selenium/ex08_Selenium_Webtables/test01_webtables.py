from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables_static():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    # get the number of rows
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = (len(row_elements))
    print(row)
    # get the number of cols
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = (len(col_elements))
    print(col)
    # //table[contains(@id,'cust')]/tbody/tr[2]/td[2]--To get teh individual elements from the static table
    # here the last two numbers only changes .We can have a For loop fro teh variable part
    # // table[contains( @ id, 'cust')] / tbody / tr[-->constant-First part
    # 2 -changes from 2 to 7-variable i
    # ]/td[-->constant-->second part
    # 2--->variable -1,2,3-j
    # ]-constant--->Third part

    first_part = "// table[contains( @ id, 'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"
    # print the element using two For loops
    for i in range(2, row + 1):  # range(1,10)--->it will take range(1,9).So we took range(1,9+1)
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text

            # code to get the country which a person belongs to in the webtable if the person is accessible
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett is in {country_text}")


# Dynamic tables
# to find elements we need to first get that table and
# //table[@summary='Sample Table']/tbody-to get only the elements we are interested in
def test_webtables_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    # using table sequencing we can find a row in teh table if the row is contained in teh table
    rows_table = table.find_elements(By.TAG_NAME,
                                     "tr")  # Or e;se you can use the "//table[@summary='Sample Table']/tbody/tr" as usual
    for row in rows_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols:
            if "UAE" in col.text:
                print("yes")
            print(f"The individual elements in the dynamic table are :{col.text}")
