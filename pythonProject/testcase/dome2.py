# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')

# driver.find_element_by_id('kw').send_keys('深圳疫情')
# time.sleep(2)
# driver.find_element_by_id("su").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="1"]/div/div[2]/a/div[2]/div[1]').click()
# time.sleep(3)
#
# driver.find_element_by_id('kw').send_keys('深圳疫情')
# time.sleep(2)
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.find_element_by_xpath('z//*[@id="1"]/div/div[2]/a/div[2]/div[1]/div[1]').click()
# driver.find_element_by_xpath('').click()
# time.sleep(5)
# driver.quit()

# 在百度登录QQ邮箱的步骤
from selenium import webdriver
import time
#使用谷歌浏览器打开百度
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#窗口最大化
driver.maximize_window()
#等待3秒
time.sleep(3)

#搜索QQ邮箱
driver.find_element_by_id('kw').send_keys('qq邮箱')
time.sleep(3)

#点击搜索
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()

handles = driver.window_handles # 获取到所有的窗口
driver.switch_to.window(handles[1])#定位到打开的QQ邮箱窗口
time.sleep(2)

#在登录的页面找到登录按钮
driver.switch_to.frame('login_frame')
time.sleep(3)
#点击账号密码按钮
rukou = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/a[2]').click()

#定位输入账号框并输入账号
driver.find_element_by_id('u').send_keys('1816199528')
#定位密码框并输入密码
driver.find_element_by_id('p').send_keys('tan199882yan')
#定位登录按钮，并点击登录
driver.find_element_by_id('login_button').click()
#
# handles = driver.window_handles # 获取到所有的窗口
# driver.switch_to.window(handles[-1])
# time.sleep(2)
# #点击写信
# driver.find.element_by_id("composebtn").click()
# time.sleep(3)
#
# #定位编辑邮件的框架
# driver.switch_to.frame('mainFrame')
# time.sleep(3)
#
# #输收件人
# driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('452990633@qq.com')
#
# #输入主题
# driver.find_element_by_id('subject').send_keys('不可以色色')
# time.sleep(3)
#
# #上传图片
# driver.find_element_by_xpath("//input[@type = 'file']").send_keys('C:\\Users\EDZ\Pictures\十元.png')
# time.sleep(3)
#
# #获取正文框架
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="qmEditorIfrmEditArea"]'))
# time.sleep(3)
#
# #输入正文内容
# driver.find_element_by_xpath("/html/body/div").send_keys('不可以色色')
# time.sleep(3)
#
# #切换到上一级
# driver.switch_to.parent_frame()
# time.sleep(3)
#
# #点击发送按钮
# driver.find_element_by_xpath("/html/body/form[2]/div[1]/div/a[1]").click()
# time.sleep(3)



