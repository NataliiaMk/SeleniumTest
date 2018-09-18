import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get ('https://www.google.com/')
assert "Google" in driver.title
element1 = driver.find_element_by_link_text('Gmail').click()
element2 = driver.find_element_by_class_name('gmail-nav__nav-link__sign-in').click()
element3 = driver.find_element_by_id('identifierId').send_keys('SupervisorTestITA@gmail.com' + Keys.ENTER)

time.sleep(5)
passwordField = driver.find_element_by_class_name('zHQkBf').send_keys('qwerty123456q' + Keys.ENTER)

time.sleep(3)
