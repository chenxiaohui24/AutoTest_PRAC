import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH,Config

#生成日志对象
class Logger():
    def __init__(self, logger_name='cowcow'):
        self.logger = logging.getLogger(logger_name)
        #该处的日志级别必须设置，否则可能无输出
        self.logger.setLevel(logging.DEBUG)
        #日志输出文件名称
        c=Config().get("log")
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'
        # 日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'INFO'
        # 日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else "fmt='%(asctime)s %(name)s %(levelname)s %(message)s'"

        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        # 避免重复日志
        if not self.logger.handlers:
            #控制台日志输出
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 输出到日志文件
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

#生成日志对象实例
logger = Logger().get_logger()

#打印日志
class Print_Logger():
    def __init__(self,logger):
        self.logger=logger

    def print_logger(self,value):
        self.logger.info("搜索 %s 完毕！" %value)





