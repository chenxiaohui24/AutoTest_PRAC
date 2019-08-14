from test.common.browser import Browser
import unittest
from utils.config import Config
from test.pages.baidu_main_page import Baidu_Main_Page

class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver=Browser().get_driver()
        self.BASE_URL=Config().get('URL')
        Baidu_Main_Page(self.driver, self.BASE_URL).get()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()