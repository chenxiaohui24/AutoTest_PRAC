from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from test.pages.page import Page
from test.common.browser import Browser

class Baidu_Main_Page(Page):
    loc_input = (By.ID, "kw")
    loc_search = (By.ID, "su")

    def __init__(self,driver,url):
        super().__init__(driver,url)

    def search(self,value):
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*self.loc_input)).send_keys(value)
        WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element(*self.loc_search)).click()

