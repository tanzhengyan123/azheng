from selenium import webdriver
import unittest
import time
class Login():
    def __init__(self,driver):
        self.driver=driver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
