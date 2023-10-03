from selenium import webdriver
from selenium.webdriver.common.by import By


class AddItems :
    link_cart_xpath = "//*[@id='shopping_cart_container']/a"


    def __init__(self,driver):
        self.driver = driver

    def click_on_cart(self):
        self.driver.find_element(By.XPATH,self.link_cart_xpath).click()


