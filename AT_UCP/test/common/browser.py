from selenium.webdriver import Remote
from selenium import webdriver
from utils.config import DRIVER_PATH

#Remote模式
# class Browser():
#     def get_driver(self):
#         dc={"browserName": "chrome",
#         "version": "",
#         "platform": "ANY",
#         "javascriptEnabled": True}
#         driver=Remote(command_executor="http://10.201.3.230:5544/wd/hub",
#                       desired_capabilities=dc)
#         return driver

#Webdriver模式
CHROME_DRIVER_PATH=DRIVER_PATH+'\chromedriver.exe'
DRIVER_TYPES={"chrome":webdriver.Chrome}

class UnSupportBrowserError(Exception):
    pass

class Browser():
    def get_driver(self,browser_type='chrome'):
        self.browser_type=browser_type.lower()
        if self.browser_type in DRIVER_TYPES:
            self.browser=DRIVER_TYPES[self.browser_type]
            driver = self.browser(executable_path=CHROME_DRIVER_PATH)
            return driver
        else:
            raise UnSupportBrowserError('不支持的类型！')



