import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service('C:/Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service = PATH)

driver.get('https://www.westpac.com.au/business-banking/services/foreign-exchange-rates/')

'''
# 等待頁面 CLASS_NAME "rowSP_Ctrl_2_2_2" 出現，才執行下方程式碼，最多等待10秒
WebDriverWait(driver, 10).until
(
    EC.presence_of_element_located((By.CLASS_NAME, "no-dropdown"))
)
'''

time.sleep(3)
rates = driver.find_element(By.CLASS_NAME, 'js-toRate')
print(f'rate:{rates.text}')


time.sleep(3)
driver.quit()
