from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://howlongtobeat.com/")
sleep(4)
trust = driver.find_element(By.ID, value="onetrust-accept-btn-handler")
trust.click()
search = driver.find_element(By.CLASS_NAME, value="MainNavigation_search_box__UUnYc")
search.send_keys("102 Dalmatians: Puppies to the Rescue", Keys.ENTER)
sleep(4)
game = driver.find_element(By.LINK_TEXT, value="102 Dalmatians: Puppies to the Rescue")
game.click()
sleep(4)

def get_info(data):
    info = driver.find_element(By.XPATH, value=f'//*[@id="__next"]/div/main/div[2]/div/div[2]/div[2]/div[{data}]')
    return process_info(info)

def process_info(data):
    result = data.text.split('\n')
    return result[1].replace(', ', '\n')

def get_time(data):
    return driver.find_element(By.XPATH, value=f'//*[@id="__next"]/div/main/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[{data}]')

genre = get_info(5)
print(genre)
platform = get_info(4)
print(platform)
year = get_info(8)
print(year)
dev = get_info(6)
print(dev)
publisher = get_info(7)
print(publisher)

avg_time = get_time(3)
print(avg_time.text)
avg_time = avg_time.text
rushed_time = get_time(5)
print(rushed_time.text)
rushed_time = rushed_time.text

art = driver.find_element(By.XPATH, value='//*[@id="__next"]/div/main/div[2]/div/div[1]/div[1]/div[1]/img').get_attribute("src")
print(art)

record_time = ...
record_holder = ...

description = driver.find_element(By.XPATH, value='//*[@id="__next"]/div/main/div[2]/div/div[2]/div[2]/div[2]')
print(description.text)
description = description.text

driver.quit()

df = pd.read_csv("game_data.csv")
df["Genre(s)"] = ""
df.loc[0, "Genre(s)"] = genre
df["Platform(s)"] = ""
df.loc[0, "Platform(s)"] = platform

df.to_csv("updated_game_data.csv", index=False)
