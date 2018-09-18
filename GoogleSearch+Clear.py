import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import string

driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get ('https://www.google.com/')
assert "Google" in driver.title
print('Google page has been opened and checked')
search1 = driver.find_element_by_name('q')
search1.send_keys('Python' + Keys.ENTER)
print('Search has been performed')

time.sleep(3)
search2 = driver.find_element_by_id('lst-ib').click()
search2 = driver.find_element_by_id('lst-ib').clear()
print('Data has been cleared')

time.sleep(5)
driver.refresh()
print('Page has been refreshed')

time.sleep(3)
driver.quit()
print("Test successfully finished")
