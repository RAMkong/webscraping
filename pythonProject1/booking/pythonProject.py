import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const

class Booking:
    def __init__(self, teardown=False):
        self.teardown = teardown

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def close_sing_in_option(self):
        some = self.driver.find_element(By.XPATH, f"//button[@aria-label='{"Dismiss sign-in info."}']")
        some.click()
    #data-testid="header-currency-picker-trigger"
    def change_currency(self, currency=None):
        currency_element = self.driver.find_element(By.XPATH, f"//button[@data-testid='{"header-currency-picker-trigger"}']")

        button_text = self.driver.find_element(By.XPATH, '//div[@class="aca0ade214 aaf30230d9 c2931f4182 e7d9f93f4d faf8b5d9a5"]/span[@class="f419a93f12"]//span[.="INR"]').text.strip()
        #xpath is found by POM builder(an extension in the browser)
        #https://pombuilder.com/
        #https://github.com/LogiGear/pombuilder.com/wiki/User-Guide

        #this checks the currency if what we wanted is already set it doesnt do anything but if the currency is different it changes the currency
        if button_text == currency:
            pass
        if button_text != currency_element:
            currency_element.click()
            selected_currency_element = self.driver.find_element(By.XPATH, f'//*[text()="{currency}"]')
            # print(selected_currency_element)
            selected_currency_element.click()

        # button_text1 = self.driver.find_element(By.XPATH, f'//*[text()="USD"]')



