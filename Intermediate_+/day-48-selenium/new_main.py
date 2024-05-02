from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://eshop-prices.com/games?currency=BRL&q=sonic")
names = driver.find_elements(By.CLASS_NAME, value="games-list-item-title")
prices = driver.find_elements(By.CLASS_NAME, value="price-tag")
games = {}
for n in range(len(names)):
    games[n] = {
        "name": names[n].text,
        "price": prices[n].text,
    }

print(games)
driver.quit()
