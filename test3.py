import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://emn178.github.io/online-tools/sha256.html"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.LINK_TEXT, "SHA224")
find.click()
delay = 2
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "input")))
print("objekts ir uz ekrana")
input()