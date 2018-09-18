import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get('https://www.google.com/')
print('Google has been opened')
element1 = driver.find_element_by_name('q').send_keys('News')
print('Query has been successfully typed')
driver.maximize_window()
print('Full screen of chrome browser')
time.sleep(2)
element2 = driver.find_element_by_name('btnK').send_keys(Keys.ENTER)
print('Button has been pressed')
time.sleep(3)
driver.quit()
print('Chrome browser has been closed')


