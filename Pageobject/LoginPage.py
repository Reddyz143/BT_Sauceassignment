import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from TestCases.conftest import setup



class Loginpage:
    txt_box_username_id = "user-name"
    txt_box_password_id = "password"
    Button_login_xpath = "//*[@id='login-button']"
    First_name = "//input[@id='first-name']"
    Last_name = "//input[@id='last-name']"
    Postal_code = "//input[@id='postal-code']"


    def __init__(self , driver):
        self.driver = driver

    def SetUserName(self,user):
        #self.driver.find_element(By.ID,self.txt_box_username_id).clear()
        self.driver.find_element(By.ID,self.txt_box_username_id).send_keys(user)

    def SetPass(self,password):
        #self.driver.find_element(By.ID,self.txt_box_password_id).clear()
        self.driver.find_element(By.ID,self.txt_box_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.Button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()

    def checkout(self):
        self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='checkout']").click()

    def input_checkouts(self):
        self.driver.find_element(By.XPATH,self.First_name ).send_keys("raju")
        self.driver.find_element(By.XPATH,self.Last_name).send_keys("reddy")
        self.driver.find_element(By.XPATH,self.Postal_code).send_keys("502372")



