import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCases.conftest import setup
from Pageobject.LoginPage import Loginpage
from Utilities.Logger import LogGen
from Pageobject.ItemSort import Itemsort
from selenium.webdriver.support.ui import Select


class Test_004_change_sortorder:
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
        self.si.option4()
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        prices = []
        for price_element in price_elements:
            price_text = price_element.text
            price = float(price_text.strip("$").replace(",", ""))  # Convert to float
            prices.append(price)

        # Verify that prices are in descending order (high to low)
        sorted_prices = sorted(prices, reverse=True)





