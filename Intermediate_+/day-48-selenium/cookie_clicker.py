from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

INTERVAL = 1 # Change for testing.
last_check_time = time.time()
numbers = "0123456789"

cookie = driver.find_element(By.ID, value="cookie")
list_of_upgrades = ["Cursor", "Grandma", "Factory", "Mine", "Shipment", "Alchemy lab", "Portal", "Time machine"]
amount = 0
i = 0

UPGRADE_LIMIT = 5 # Change for testing.

def buy_upgrade(upgrade):
    value = f"buy{upgrade}"
    element = driver.find_element(By.ID, value=value)
    buy_number = [char for char in element.text[:29] if char in numbers]
    buy_price = "".join(buy_number)
    return element, buy_price

while True:
    current_time = time.time()
    if current_time - last_check_time >= INTERVAL:
        if amount < UPGRADE_LIMIT:
            last_check_time = current_time
            money = driver.find_element(By.ID, value="money")
            element, buy_price = buy_upgrade(list_of_upgrades[i])
            print(int(buy_price))
            if int((money.text).replace(",", "")) >= int(buy_price):
                element.click()
                amount += 1
        elif i< len(list_of_upgrades):
            i += 1
            amount = 0
        else:
            break
    cookie.click()
    time.sleep(0.01)

time.sleep(5)
print("Success")
# driver.quit()
