from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def close_first_ad():
    blank = driver.find_element(By.XPATH, value="/html")
    blank.click()
    sleep(1)
    target_tab = driver.window_handles[0]
    ad_tab = driver.window_handles[1]
    driver.switch_to.window(ad_tab)
    driver.close()
    driver.switch_to.window(target_tab)
    sleep(1)

def download():
    cookie = driver.find_element(By.CLASS_NAME, value="download")
    cookie.click()

with open("links.txt", "r") as data:
    content = data.readlines()

for n in range(len(content)):
    if n == 0:
        continue
    driver.get(content[n])
    close_first_ad()
    download()
    sleep(16)
    close_first_ad()
    close_first_ad()
    download()
    sleep(60)

driver.quit()
