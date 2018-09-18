import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get('https://www.google.com.ua/')
element1 = driver.find_element_by_name('btnI')
element1.click()

element2 = driver.find_element_by_id('language-menu').click()

select = Select(driver.find_element_by_name('hl'))

select.select_by_value('ru')
print('Ru selected')

element3 = driver.find_element_by_id('searchinput').send_keys('День независимости Украины 2018' + Keys.ENTER)
time.sleep(5)
element4 = driver.find_element_by_id('archive-link').click()

time.sleep(3)
driver.quit()

#id('lang-chooser')
