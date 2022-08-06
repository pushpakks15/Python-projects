from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Development/chromedriver.exe"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com/")
time.sleep(8)
cookies=driver.find_element(By.XPATH,'//*[@id="q554704800"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
login=driver.find_element(By.XPATH,'//*[@id="q554704800"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(5)
loginwithgoogle=driver.find_element(By.XPATH,'//*[@id="q-1173676276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
loginwithgoogle.click()
time.sleep(5)


base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)

email=driver.find_element(By.XPATH,'//*[@id="email"]')
email.send_keys("xabc31480@gmail.com")
password=driver.find_element(By.ID,"pass")
password.click()
password.send_keys("2249517")
logintofb=driver.find_element(By.ID,"loginbutton")
logintofb.click()

