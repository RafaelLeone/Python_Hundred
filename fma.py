from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.anitube.vip/download/animes-dublado/fullmetal-alchemist-brotherhood-dublado")

NUMBER_OF_EPISODES = 64
episode = 12

with open("links.txt", "w") as data:
    for i in range(episode, NUMBER_OF_EPISODES+1):
        cookie = driver.find_element(By.XPATH, value=f"/html/body/div[3]/div[1]/table/tbody/tr[{i}]/td[3]/p/a")
        episode_link = cookie.get_attribute("href")
        data.write(f"\n{episode_link}")

driver.quit()
