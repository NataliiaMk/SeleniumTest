import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Chrome_webdriver\chromedriver.exe')

driver.get('https://www.google.com')
assert "Google" in driver.title
print('Google page has been opened and checked')
element1 = driver.find_element_by_name('q').send_keys('Wikipedia')
print('Queri has been successfully typed')
element2 = driver.find_element_by_name('btnI').send_keys(Keys.ENTER)
print('Button has been pressed')
time.sleep(3)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
print('Scroll-down')
time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
print('Scroll-up')
time.sleep(2)
driver.quit()
print('Chrome browser has been closed')
