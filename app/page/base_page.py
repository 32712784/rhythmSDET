# coding=utf-8
from time import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

class BasePage:
    # 输出日志不能实时打印出来，不知道为啥
    # root_logger = logging.getLogger()
    # print(f"root_logger.handlers:{logging.getLogger().handlers}")
    # for h in root_logger.handlers[:]:
    #     root_logger.removeHandler(h)
    # logging.basicConfig(level=logging.INFO)

    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def log(self):
        # 创建logger，如果参数为空则返回root logger
        logger = logging.getLogger("test")
        logger.setLevel(logging.DEBUG)  # 设置logger日志等级

        # 如果存在logger.handlers列表为0，则创建handler
        if len(logger.handlers) == 0:
            # 创建handler
            # fh = logging.FileHandler("log.txt", encoding="utf-8")  # 输出日志保存到文件
            ch = logging.StreamHandler()  # 日志打印到窗口

            # 设置输出日志格式
            formatter = logging.Formatter(
                fmt="%(asctime)s %(name)s %(filename)s %(message)s",
                datefmt="%Y/%m/%d %X")

            # 为handler指定输出格式
            # fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 为logger添加的日志处理器
            # logger.addHandler(fh)
            logger.addHandler(ch)

        # 直接返回logger
        return logger

    def find(self, by, locator):
        # self.log().info(by)
        self.log().info(by)
        self.log().info(locator)
        return self.driver.find_element(by,locator)

    def finds(self, by, locator):
        self.log().info(by)
        self.log().info(locator)
        return self.driver.find_elements(by,locator)

    # 根据控件的text，滚动查找并点击
    def find_by_scroll(self, text):
        self.log().info('find_by_scroll')
        self.log().info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def wait_element_visibility(self,by,locator):
        self.log().info(by)
        self.log().info(locator)
        WebDriverWait(self.driver, 5).until(lambda x : x.find_element(by, locator))
        return self.find(by, locator)

    def wait_element_invisible(self,by,locator):
        self.log().info(by)
        self.log().info(locator)
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((by,locator)))

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

