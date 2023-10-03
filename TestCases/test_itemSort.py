
import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCases.conftest import setup
from Pageobject.LoginPage import Loginpage
from Utilities.Logger import LogGen
from Pageobject.ItemSort import Itemsort
from selenium.webdriver.common.keys import Keys


class Test_003_item_validation:
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
        self.default = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[1]")
        status = (self.default.is_selected())
        if status:
            item_elements = self.driver.find_elements(By.XPATH, "//*[@id='item_[0-5]_title_link']/div")
            item_names = [item.text for item in item_elements]
            is_sorted = item_names == sorted(item_names)
            if is_sorted is True:
                print("Items are in alphabetical order.")
            else:
                print("Items are not in alphabetical order.")




