import HTMLTestRunnerCN
import unittest
Testcase_dir = 'C:\\Users\\1\\PycharmProjects\\pythonProject\\testcase'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'qqq.py')
# 定义报告存放路径
filename = "C:\\Users\\1\PycharmProjects\pythonProject\\baogao\\result.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
    # 运行测试用例
runner.run(dis)
#关闭报告文件
#fp.close()