import os
from selenium import webdriver

os.environ['PATH'] += r'C:\Users\cvsri\Downloads\chrome-win32\chrome_proxy.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://chapmanganato.to/manga-ax951880/chapter-464.1")

driver.implicitly_wait(5)
# try:
#     no_button = driver.find_element_by_class_name('at-cm-no-button')
#     no_button.click()
# except:
#     print('No element with this class name. Skipping ....')

# sum1 = driver.find_element_by_id('sum1')
# sum2 = driver.find_element_by_id('sum2')
#
# sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
# sum2.send_keys(15)
#
# btn = driver.find_element('css_selector','button[onclick="PREV CHAPTER"]')
# btn.click()
# name = driver.find_element("class","navi-change-chapter-btn-prev a-h")
# name.click()
some=driver.find_element("div","navi-change-chapter-btn-prev a-h")
print(some)
