import wget
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


f1 = open("output.csv", "r")
recommendations = f1.read().split('\n')
f1.close()

f2 = open("followed.csv", "r")
followed = f2.read().split('\n')
f2.close()

followed = [x.split('|')[0] for x in followed]

to_follow = [x for x in recommendations if x not in followed]

# Username - mlnc_confessions_
# Password - MLAconfess@

driver = webdriver.Chrome()

driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("iisb_confessions")
password.clear()
password.send_keys("qwerty.1234")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)

try:
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(text(), "Not now")]'))).click()
except:
    pass

time.sleep(2)

try:
    alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
except:
    pass

# to_follow=['rbansal99']--------------------------------------------------------------------------------
import random

print()

f1 = open('followed.csv','r')
l1 = f1.readlines()
# print(l1)
l2 =[]
for l3 in l1:
    l2.append(l3[:-3])
# print(l2)

for user in to_follow:
#   break
  try:
    if user in l2:
        continue
    print(user)
    driver.get('https://www.instagram.com/'+ user)

    time.sleep(random.uniform(60,65))

    # searchbox = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    # searchbox.clear()

    # for x in user:
    #     time.sleep(0.2)
    #     searchbox.send_keys(x)

    # time.sleep(2)

    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    #     (By.XPATH, '//div[text()="' + user + '"]'))).click()
    # time.sleep(2)
    f3 = open("followed.csv", "a")
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Follow']"))).click()
        
        
        try:
            private = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                (By.XPATH, '//h2[contains(text(), "This Account is Private")]'))).click()
            f3.write(user + '|0' + '\n')
        except:
            try:
                private_2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                    (By.XPATH, '//h2[contains(text(), "This account is private")]'))).click()
                f3.write(user + '|0' + '\n')
            except:
                f3.write(user + '|1' + '\n')
        
    except:
        f3.write(user + '|-1' + '\n')
        pass
    f3.close()
  except:
    pass

driver.quit()
