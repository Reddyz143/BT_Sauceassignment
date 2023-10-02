
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestCases.conftest import setup
from Pageobject.LoginPage import Loginpage
from selenium.webdriver.chrome.service import Service
from Utilities.Logger import LogGen


class Test_002_login :

    Base_url = "https://www.saucedemo.com/"
    user = "locked_out_user"
    password = "secret_sauce"

    logger = LogGen.loggen()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.lp = Loginpage(self.driver)
        self.lp.SetUserName(self.user)
        self.lp.SetPass(self.password)
        self.lp.clickLogin()
        Error = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        status = Error.is_displayed()
        print(status)
        if status == True:
            self.logger.info("************* verified login unsucessful ***************")
            assert True
        else:
            assert False