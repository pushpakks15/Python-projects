from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


import time

chrome_driver_path = "C:/Development/chromedriver.exe"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)
cookie = driver.find_element(By.ID, value="cookie")

five_mins = time.time() + 5*60
timeout = time.time() + 8

while time.time() < five_mins:
    cookie.click()
if time.time() > timeout:
    money_element = driver.find_element(By.ID, value="money")
    money = int(money_element.text.replace(",", ""))
    prices_list = driver.find_elements(By.XPATH, value=".//*[contains(@id, 'buy')]")
    ids = [price.get_attribute("id") for price in prices_list]
    ids.remove("buyElder Pledge")
    prices = []
    affordable_upgrades = []
    upgrades_dict = {}
for price in prices_list:
    try:
        prices.append(int(price.text.split("-")[1].strip().split("\n")[0].replace(",", "")))
    except IndexError:
        continue
        for i in range(0, len(prices)):
            upgrades_dict[f"{prices[i]}"] = f"{ids[i]}"
            if money >= prices[i]:
                affordable_upgrades.append(prices[i])
                the_highest_affordable_one = max(affordable_upgrades)
                print(the_highest_affordable_one)
                affordable_id = upgrades_dict[f"{the_highest_affordable_one}"]
                id_to_click = driver.find_element(By.ID, value=affordable_id)
                print(affordable_id)
                id_to_click.click()
                timeout = time.time() + 8
            else:
                cookies_per_second = driver.find_element(By.ID, value="cps")
                print(cookies_per_second.text)
driver.quit()


