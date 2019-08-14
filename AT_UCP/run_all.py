import unittest
import time,os
from utils.config import REPORT_PATH,TEST_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Send_Mail
from test.suite.suites import Suite

if __name__ == '__main__':
    now=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
    report = os.path.join(REPORT_PATH +'\\')+now+' report.html'
    if os.path.exists(REPORT_PATH):
        with open(report, 'wb') as f:
            runner = HTMLTestRunner(stream=f,verbosity=2,title='从0搭建测试框架 cowcow', description='百度搜索测试报告20190808')
            runner.run(Suite)
        Send_Mail("18217023178@163.com","uc123123").send_mail()
    else:
        print("测试报告存放路径不存在！！！")