from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random
import os 
from dotenv import load_dotenv
import pyperclip

# 셀레늄 설정
load_dotenv(override=True)

LOGIN_ID = os.getenv('LOGIN_ID')
LOGIN_PW = os.getenv('LOGIN_PW')

url = 'https://nid.naver.com/nidlogin.login'


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.get(url)

# id 입력
id_input = driver.find_element(By.ID, "id")
pyperclip.copy(LOGIN_ID)
id_input.click()
id_input.send_keys(Keys.CONTROL, 'v')
time.sleep(random. uniform(1.5, 3.5))

# pw 입력
id_pw = driver.find_element(By.ID, "pw")
pyperclip.copy(LOGIN_PW)
id_pw.click()
id_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(random. uniform(1.5, 3.5))

# 로그인 버튼 클릭
login_btn = driver.find_element(By.ID, "log.login")
login_btn.click()
time.sleep(random. uniform(1.5, 3.5))

# 글작성 페이지 이동
driver.get("https://blog.naver.com/GoBlogWrite.naver")
time.sleep(random. uniform(1.5, 3.5))

time.sleep(10)
driver.quit()