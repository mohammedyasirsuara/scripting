#Selenium
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\Program Files (x86)\msedgedriver.exe")
driver = webdriver.Edge(service=PATH)

def twitterBot():
    try:
        driver.get("https://twitter.com/login")

        # Enter username in Field
        uName = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username"]'))
        )
        uName.send_keys('xxxxxx')
        driver.implicitly_wait(5)

        # Click the next button
        nButton = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        nButton.click()
        driver.implicitly_wait(5)

        # Input password
        # pWord = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"')
        # pWord.send_keys('xxxx')
        # driver.implicitly_wait(5)
        pWord = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]'))
        )
        pWord.send_keys('xxxxxxx')

        #Login
        lButton = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div')
        lButton.click()

        # for article ingit articles:
        #     header = article.find_element(By.CLASS_NAME, "entry-summary")
        #     print(header.text)
    except:
        driver.quit()

# Call function
twitterBot()