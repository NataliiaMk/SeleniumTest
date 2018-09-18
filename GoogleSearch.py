from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:\Chrome_webdriver\chromedriver.exe")

driver.get("https://www.google.com.ua/")
print("Google has opened")
driver.maximize_window()
print("Windom has maximized")
driver.find_element_by_name("q").send_keys("Selenium" + Keys.ENTER)
print("Search has been performed")
driver.quit()
print("Test successfully finished")


