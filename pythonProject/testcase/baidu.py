# from selenium import webdriver
# import time
# driver = webdriver.Chrome()

# driver.get('https://www.baidu.com')
# driver.maximize_window()
# driver.find_element_by_id('kw').send_keys('sss')
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.quit()

# driver.get('https://www.baidu.com')
# driver.maximize_window()
# driver.find_element_by_id('kw').send_keys('京东')

# from selenium import webdriver
# import time
#
# class Mylib():
#
#     def __init__(self):
#         #初始化浏览器对象
#         self.driver = webdriver.Chrome()
#
#     def delay(self):
#         #延迟等待
#         self.driver.implicitly_wait(5)
#
#     def open_url(self, url):
#         #访问网站
#         self.driver.get(url)
#         self.delay()
#         print('访问:%s成功'%url)
#
#     def locate_element(self, locate_type, value):
#
#         return self.driver.find_element(locate_type,value)
#         #return self.driver.locate_element(locate_type,value)
#
#     def __del__(self):
#         time.sleep(5)
#         self.driver.close()
#
# if __name__ == '__main__':
#     web = Mylib()
#     web.open_url('https://www.baidu.com')
#     el = web.locate_element('id','kw')
#     el.send_keys('itcast')
#     el_sub = web.locate_element('id','su')
#     el_sub.click()


from selenium import webdriver
import time
class Mylib():
    def __init__(self):
        self.drive = webdriver.Chrome()
     def delay(self):
        self.drive.implicitly_wait(4)















