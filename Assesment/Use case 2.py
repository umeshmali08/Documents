#Use case 2

import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj =Service("C:/Users/dell/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button").click()
act_title = driver.title
exp_title ="OrangeHRM"

if act_title == exp_title:
    print("Login Test Pass")

else:
    print("Login Test Fail")

    driver.quit()