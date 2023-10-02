from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service



@pytest.fixture()

def setup():
        s = Service("C:/Users/Tony Stark/Downloads/chromedriver2.exe")
        driver = webdriver.Chrome(service=s)
        print("launching chrome browser.............")
        return driver