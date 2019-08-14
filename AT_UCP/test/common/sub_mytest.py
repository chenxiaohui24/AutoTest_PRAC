from test.common.browser import Browser
import unittest
from utils.config import Config
from test.pages.baidu_main_page import Baidu_Main_Page

class Sub_Mytest(unittest.TestCase):
    def sub_setUp(self):
        self.driver = Browser().get_driver()
        self.BASE_URL = Config().get('URL')
        Baidu_Main_Page(self.driver, self.BASE_URL).get()

    def sub_tearDown(self):
        self.driver.quit()