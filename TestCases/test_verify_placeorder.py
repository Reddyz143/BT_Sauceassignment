import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCases.conftest import setup
from Pageobject.LoginPage import Loginpage
from Pageobject.ItemSort import Itemsort
from selenium.webdriver.support.ui import Select


import random
from Pageobject.AdditemsPage import AddItems



class Test_006_placeorder:
    Base_url = "https://www.saucedemo.com/"
    user = "standard_user"
    password = "secret_sauce"



    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.driver.implicitly_wait(5)
        self.lp = Loginpage(self.driver)
        self.lp.SetUserName(self.user)
        self.lp.SetPass(self.password)
        self.lp.clickLogin()

        self.si = Itemsort(self.driver)
        self.si.click_on_filter()
        time.sleep(5)
        self.si.option4()
        self.si.hiloitem()
        self.si.lohiitem()
        self.lp.checkout()
        self.lp.input_checkouts()
        self.driver.find_element(By.XPATH, "//*[@id='continue']").click()
        Total_price = self.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]")
        if Total_price is not None:
            print("total price value is working")
        else:
            print("total price is not working")
        self.driver.find_element(By.XPATH, "//*[@id='finish']").click()
        confirmation_message = self.driver.find_element(By.CSS_SELECTOR, ".complete-header").text
        print(f"Order Confirmation: {confirmation_message}")
        back_home_button = self.driver.find_element(By.XPATH, "//button[@id='back-to-products']")
        back_home_button.click()

