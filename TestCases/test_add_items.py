import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCases.conftest import setup
from Pageobject.LoginPage import Loginpage
from Pageobject.ItemSort import Itemsort
import random
from Pageobject.AdditemsPage import AddItems



class Test_005_AddItems:
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

        product_identifiers = [
            "//*[@id='add-to-cart-sauce-labs-backpack']",
            "//*[@id='add-to-cart-sauce-labs-bike-light']",
            "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
            "//*[@id='add-to-cart-sauce-labs-fleece-jacket']",
            "//*[@id='add-to-cart-sauce-labs-onesie']"
            ]
        sample_size = min(3, len(product_identifiers))
        selected_identifiers = random.sample(product_identifiers, sample_size)
        for identifier in selected_identifiers:
            self.driver.find_element(By.XPATH, identifier).click()
            time.sleep(10)
        self.lp.clickLogout()

        self.driver = setup
        self.driver.get(self.Base_url)
        self.driver.implicitly_wait(5)
        self.lp = Loginpage(self.driver)
        self.lp.SetUserName(self.user)
        self.lp.SetPass(self.password)
        self.lp.clickLogin()

        self.add = AddItems(self.driver)
        self.add.click_on_cart()

        cart_element = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a/span")
        cart_text = cart_element.text
        num_items_in_cart = int(cart_text)
        print(f"Number of items in the cart: {num_items_in_cart}")







