import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import string

driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get ('https://www.google.com/')
assert "Google" in driver.title
search1 = driver.find_element_by_name('q')
search1.send_keys('Python' + Keys.ENTER)
time.sleep(3)
search2 = driver.find_element_by_id('lst-ib').click()
search2 = driver.find_element_by_id('lst-ib').clear()
time.sleep(2)
driver.refresh()
time.sleep(3)
driver.quit()
