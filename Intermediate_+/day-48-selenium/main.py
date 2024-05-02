from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

games = [
    "https://eshop-prices.com/games?currency=BRL&q=persona+3+portable",
    "https://eshop-prices.com/games?currency=BRL&q=crisis+core+final+fantasy+vii+reunion",
    "https://eshop-prices.com/games?currency=BRL&q=disney+classic+games+aladdin+and+the+lion+king",
    "https://eshop-prices.com/games?currency=BRL&q=klonoa+phantasy+reverie+series",
    "https://eshop-prices.com/games?currency=BRL&q=pac-man+world+re-pac",
    "https://eshop-prices.com/games?currency=BRL&q=kingdom+hearts+melody+of+memory",
]

for game in games:
    driver.get(game)
    name = driver.find_element(By.CLASS_NAME, value="games-list-item-title")
    price = driver.find_element(By.CLASS_NAME, value="price-tag")
    print(f"The price for {name.text} is {price.text} reais.")

driver.quit()
