from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Development/chromedriver.exe"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3203582769&f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")
sign=driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
sign.click()


email=driver.find_element(By.ID,"username")

email.send_keys("pushpak.22010400@viit.ac.in")
password=driver.find_element(By.ID,"password")

password.send_keys("22495717")
sign_in_button=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("7709266305")

        submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
