from selenium import webdriver
import time #添加时间
class Youxiang():  #创建一个类 叫邮箱
    def __init__(self,driver):  #初始化驱动
        self.driver=driver

    def You(self,username,pws):  #将’u‘，’p'变成可变量
        self.driver.find_element_by_id("u").send_keys(username)
        self.driver.find_element_by_id("p").send_keys(pws)
        self.driver.find_element_by_id('login_button').click()  #点击登录
        time.sleep(5)
