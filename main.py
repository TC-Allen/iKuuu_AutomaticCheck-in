import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get('https://ikuuu.me/user')
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-lg.btn-block.login').click()

WebDriverWait(driver, 60).until(EC.url_changes(driver.current_url))
driver.find_element(By.ID, 'checkin-div').click()
driver.quit()
