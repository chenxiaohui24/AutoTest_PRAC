import zmail
import os
from utils.config import REPORT_PATH
#coding=utf-8
class Send_Mail():
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def send_mail(self):
        #定义邮箱服务
        server=zmail.server(username=self.username,password=self.password)

        #定义邮件内容
        #以列表形式列出目录下所有测试报告文件
        lists=os.listdir(REPORT_PATH)
        #对测试报告文件以倒序排列，并且取最新的报告
        lists.sort(key=lambda fn:os.path.getctime(REPORT_PATH+"\\"+fn))
        newest_report = lists[-1]
        report = os.path.join(REPORT_PATH, newest_report)
        #构造邮件内容
        with open(report,'r',encoding='UTF-8') as f:
            content_html = f.read()
        mail={'subject':'selenium测试框架报告',
        'content_text':'测试框架终于搭建完成，并且测试结果OK！！',
        'content_html':content_html,
        'attachments':['C:\\Users\chenx\Desktop\IMG_5565.JPG',],
        'from':'cowcow<18217023178@163.com>'}

        #发送邮件
        server.send_mail([('陈晓辉','chenxiaohui@uce.cn'),],mail)