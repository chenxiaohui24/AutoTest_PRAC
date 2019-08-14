import time
import unittest
from utils.config import Config, DATA_PATH,DRIVER_PATH
from utils.log import Print_Logger,logger
from utils.file_reader import ExcelReader
from utils.screen_shot import Screen_Shot
from test.pages.baidu_main_page import Baidu_Main_Page
from test.common import sub_mytest

class TestBaiDu(sub_mytest.Sub_Mytest):
    """百度搜索测试B"""
    excel = DATA_PATH + '/baidu.xlsx'

    def test_search_2(self):
        """百度搜索B1"""
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                #环境初始化
                self.sub_setUp()
                #测试用例
                Baidu_Main_Page(self.driver, self.BASE_URL).search(d['search'])
                time.sleep(3)
                # 截图
                Screen_Shot(self.driver).save_screen_shot()
                # 打印日志
                Print_Logger(logger).print_logger(d['search'])
                #环境清理
                self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()
