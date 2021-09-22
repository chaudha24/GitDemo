from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver =webdriver.Chrome(r"C:\Users\chauda14\PycharmProjects\SeleniumProject\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("javapoint")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.close();
print(" Sample test successfully completed")