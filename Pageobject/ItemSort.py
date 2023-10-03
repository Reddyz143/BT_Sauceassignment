from selenium import webdriver
from selenium.webdriver.common.by import By


class Itemsort :
    filter_dropdown_Xpath = "//*[@id='header_container']/div[2]/div/span/select"
    A_Z_01_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[1]"
    Z_A_02_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[2]"
    low_high_03_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[3]"
    high_low_04_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[4]"
    item_names_Xpath = "//*[@id='item_[0-5]_title_link']/div"
    hilo_first_item = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    lohi_first_item = "//button[@id='add-to-cart-sauce-labs-onesie']"

    def __init__(self,driver):
        self.driver = driver

    def click_on_filter(self):
        self.driver.find_element(By.XPATH,self.filter_dropdown_Xpath).click()

    def option1(self):
        self.driver.find_element(By.XPATH,self.A_Z_01_xpath).click()
    def option2(self):
        self.driver.find_element(By.XPATH,self.Z_A_02_xpath).click()
    def option3(self):
        self.driver.find_element(By.XPATH,self.low_high_03_xpath).click()
    def option4(self):
        self.driver.find_element(By.XPATH,self.high_low_04_xpath).click()
    def hiloitem(self):
        self.driver.find_element(By.XPATH, self.hilo_first_item).click()
    def lohiitem(self):
        self.driver.find_element(By.XPATH, self.lohi_first_item).click()





