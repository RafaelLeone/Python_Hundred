from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

games = [
    "https://eshop-prices.com/games?currency=BRL&q=persona+3+portable",
    "https://eshop-prices.com/games?currency=BRL&q=crisis+core+final+fantasy+vii+reunion",
]

for game in games:
    driver.get(game)
    price = driver.find_element(By.CLASS_NAME, value="price-tag")
    print(f"The price for {game[46:]} is {price.text} reais.")

driver.quit()
