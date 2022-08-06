from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:/Development/chromedriver.exe"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
URL = "https://www.google.com"
driver.get(URL)
input=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
input.click()
input.send_keys("www.youtube.com")
input.send_keys(Keys.ENTER)
