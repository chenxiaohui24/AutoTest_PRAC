import os
import time
from utils.config import SCREENSHOT_PATH


class Screen_Shot():
    #初始化
    def __init__(self,driver):
        self.driver=driver
     #保存截图
    def save_screen_shot(self):
        self.current_time=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
        self.screenshot_path=SCREENSHOT_PATH
        self.image_name =self.screenshot_path+'\\'+ self.current_time + '.png'
        if not os.path.exists(self.screenshot_path):
            os.mkdir(self.screenshot_path)
        try:
            print("开始截图————")
            self.driver.get_screenshot_as_file(self.image_name)
            print("截图完成————")
            print("截图保存在："+SCREENSHOT_PATH)
        except Exception as e:
            print(e)

