import time
import unittest
from utils.log import Print_Logger,logger
from utils.screen_shot import Screen_Shot
from test.pages.baidu_main_page import Baidu_Main_Page
from test.common import mytest

class TestBaiDu(mytest.Mytest):

    def test_search_5(self):
        """百度搜索A3"""
        #测试用例
        Baidu_Main_Page(self.driver, self.BASE_URL).search('Pytest')
        time.sleep(3)
        #截图
        Screen_Shot(self.driver).save_screen_shot()
        # 打印日志
        Print_Logger(logger).print_logger('Pytest')

    def test_search_6(self):
        """百度搜索A4"""
        #测试用例
        Baidu_Main_Page(self.driver, self.BASE_URL).search('ADB')
        time.sleep(3)
        # 截图
        Screen_Shot(self.driver).save_screen_shot()
        # 打印日志
        Print_Logger(logger).print_logger('ADB')

if __name__ == '__main__':
    unittest.main()



