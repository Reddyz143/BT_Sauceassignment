import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCases.conftest import setup
from Pageobject.LoginPage import Loginpage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class Test_001_login :
    Base_url = "https://www.saucedemo.com/"
    user1 = "standard_user"
    user2 = "performance_glitch_user"
    password = "secret_sauce"

    def test_homepagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.driver.implicitly_wait(2)
        actl_Title = self.driver.title
        if actl_Title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.lp = Loginpage(self.driver)
        self.lp.SetUserName(self.user1)
        self.lp.SetPass(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            self.lp.clickLogout()
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshorts\\+homepage.png')
            self.driver.close()
            assert False

    def test_login_user2(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.lp = Loginpage(self.driver)
        self.lp.SetUserName(self.user2)
        self.lp.SetPass(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            self.lp.clickLogout()
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshorts\\+homepage.png')
            self.driver.close()
            assert False