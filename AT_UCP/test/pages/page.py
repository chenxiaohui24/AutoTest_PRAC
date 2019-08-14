from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test.common.browser import Browser

class Page():
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url

    def get(self,maximize_window=True):
        self.driver.get(self.url)
        if maximize_window:
            self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

