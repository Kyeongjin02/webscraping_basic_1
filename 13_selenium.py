from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(options=options) # service=service, options=options

# 1. 네이버 이동
url = "https://naver.com"
browser.get(url)

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, 'link_login')
elem.click() 

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("naver_pw")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료
