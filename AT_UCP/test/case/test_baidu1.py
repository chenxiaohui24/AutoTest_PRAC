import time
from utils.log import Print_Logger,logger
from utils.screen_shot import Screen_Shot
from test.pages.baidu_main_page import Baidu_Main_Page
from test.common import mytest

class TestBaiDu(mytest.Mytest):
    """百度搜索测试A"""
    def test_search_0(self):
        """百度搜索A1"""
        #测试用例
        Baidu_Main_Page(self.driver, self.BASE_URL).search('Linux')
        time.sleep(3)
        #截图
        Screen_Shot(self.driver).save_screen_shot()
        #打印日志
        Print_Logger(logger).print_logger('Linux')

    def test_search_1(self):
        """百度搜索A2"""
        #测试用例
        Baidu_Main_Page(self.driver, self.BASE_URL).search('Python')
        time.sleep(3)
        # 截图
        Screen_Shot(self.driver).save_screen_shot()
        # 打印日志
        Print_Logger(logger).print_logger("Python")





