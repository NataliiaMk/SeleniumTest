import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get ('https://www.google.com/')
assert "Google" in driver.title
element1 = driver.find_element_by_link_text('Зображення').click()
time.sleep(2)
element2 = driver.find_element_by_id('qbi').click()
element3 = driver.find_element_by_id('qbui').send_keys('https://www.google.com.ua/search?q=%D0%B1%D0%B0%D0%B3&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjmtf3OkMPdAhWFBSwKHUTTCRAQ_AUICigB&biw=1366&bih=626#imgrc=YyBugC7IfvFcmM:')
element4 = driver.find_element_by_id('qbbtc').click()
element5 = driver.find_element_by_id('lst-ib').send_keys('Баг' + Keys.ENTER)
element6 = driver.find_element_by_link_text('Усі').click()
time.sleep(3)
driver.quit()

