from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Development/chromedriver.exe"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://twitter.com/")
