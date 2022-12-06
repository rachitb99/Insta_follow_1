import random
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
directory = 'accounts'

existing = []

for filename in os.listdir(directory):
    existing.append(filename[:-14])

f2 = open("followed.csv", "r")
followed = f2.read().split('\n')
f2.close()


followed = [x.split('|') for x in followed if x!='']

followed = [x[0] for x in followed if x[1] == '1']

to_get_followers = [x for x in followed if x not in existing]

options = Options()
options.add_argument("--kiosk")
options.add_extension("/Users/rachitbansal/Downloads/instagram_stonehill/extension.crx")

driver = webdriver.Chrome(chrome_options=options)

driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("crush.cu")
password.clear()
password.send_keys("CrushingIT132@")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(10)

for i,account in enumerate(to_get_followers):
    # account = 'we_are_slick'
    
    driver.get('chrome-extension://nmnhoiehpdfllknopjkhjgoddkpnmfpa/html/export.html?user=' + account)
    if i==0:
        time.sleep(100)
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Start parsing']"))).click()
        WebDriverWait(driver, 200).until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Finished']"))).click()
        if driver.find_element(By.ID, 'statusProfiles').text == "0":
            time.sleep(6)
            continue
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Save to CSV']"))).click()
        time.sleep(10)
        try:
            os.system('mv /Users/rachitbansal/Downloads/{}_followers.csv /Users/rachitbansal/Downloads/instagram_stonehill/accounts'.format(account))
        except:
            print('File not moved.')
        time.sleep(random.uniform(50,55))
        
        
    except Exception as err:
        print(err)
        print('crashed')
        time.sleep(20)
        pass
