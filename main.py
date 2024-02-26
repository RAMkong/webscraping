import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

os.environ['PATH'] += r'C:\Users\cvsri\Downloads\chrome-win32\chrome_proxy.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/download")

driver.implicitly_wait(5)

some=driver.find_element(By.LINK_TEXT,'Test1.pdf')
some.click()