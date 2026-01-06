from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os 
import time

load_dotenv()
driver = webdriver.Chrome()

driver.get("https://example.com")

title = driver.find_element(By.TAG_NAME, 'h1').text
ptage = driver.find_element(By.TAG_NAME, 'p').text

print(title)
print(ptage)


secret_key = os.getenv('SECRET_KEY')


print(secret_key)
time.sleep(1)
driver.quit()


