import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get ('https://www.google.com/')
assert "Google" in driver.title
print('Google page has been opened and checked')

element1 = driver.find_element_by_link_text('Gmail').click()
print('Gmail tab has been opened')
element2 = driver.find_element_by_class_name('gmail-nav__nav-link__sign-in').click()
print('Sign in button has been pressed')
element3 = driver.find_element_by_id('identifierId').send_keys('SupervisorTestITA@gmail.com' + Keys.ENTER)
print('user id has been entered')

time.sleep(5)
passwordField = driver.find_element_by_class_name('zHQkBf').send_keys('qwerty123456q' + Keys.ENTER)
print('user password has been entered')

time.sleep(5)

driver.quit()
print('Chrome browser has been closed')
