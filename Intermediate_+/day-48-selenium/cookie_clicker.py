from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
last_check_time = time.time()
INTERVAL = 0.5

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

buy_cursor = driver.find_element(By.ID, value="buyCursor")
buy_cursor_number = [letter for letter in buy_cursor.text[:29] if letter in numbers]
buy_cursor_price = "".join(buy_cursor_number)
cursor_amount = 0

while True:
    current_time = time.time()
    if current_time - last_check_time >= INTERVAL:
        last_check_time = current_time
        money = driver.find_element(By.ID, value="money")
        buy_cursor = driver.find_element(By.ID, value="buyCursor")

        buy_cursor_number = [letter for letter in buy_cursor.text[:29] if letter in numbers]
        buy_cursor_price = "".join(buy_cursor_number)
        if cursor_amount >= 99:
            break # TO DO: add other upgrades instead of breaking.
        elif int(money.text) >= int(buy_cursor_price):
            buy_cursor.click()
            cursor_amount += 1
    cookie.click()
    time.sleep(0.01)

time.sleep(5)
print("Success")
driver.quit()
