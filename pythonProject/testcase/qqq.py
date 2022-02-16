from selenium import webdriver
import time
import unittest
class Baidu_Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

    def test_baidu_seach(self):
        self.driver.find_element_by_id('kw').send_keys('china')
        time.sleep(3)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()