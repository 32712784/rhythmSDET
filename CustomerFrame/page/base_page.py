# coding=utf-8
from time import sleep

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.android.webdriver import WebDriver

from rhythmSDET.CustomerFrame.page.hand_black import hand_black


class BasePage:
    black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    iter_max=3
    error_num=0

    def __init__(self, driver: WebDriver = None):
        # driver为空则新建
        if driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "Autotest"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".common.MainActivity"
            # 此参数设置后，执行完用例不会关闭APP
            caps["dontStopAppOnReset"] = True
            # 不加此参数，会需要登录
            caps["noReset"] = "True"
            # 跳过设备初始化，加快执行速度
            caps["skipDeviceInitialization"] = True
            # 跳过服务安装初始化
            caps["skipServerInstallation"] = True
            # 中文输入内容时，需要提前设置
            caps["unicodeKeyBoard"] = "True"
            caps["resetKeyBoard"] = "True"
            # 设置全局idle等待时间为0
            caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            # 复用driver
            self.driver = driver

    def quit_app(self):
        self.driver.quit()

    @hand_black
    def find(self, by, locator = None):
        if locator ==None:
            element = self.driver.find_element(*by)
        else:
            element = self.driver.find_element(by,locator)
        return element

    # 通过yaml文件配置方法中需要操作的元素，然后通过yaml解析，进行操作
    def parse_yaml(self,path,func,value=""):
        with open(path) as f:
            datas = yaml.load(f)
        # steps = [{'by': 'id', 'locator': 'com.xueqiu.android:id/post_status', 'action': 'click'}, {'by': 'xpath', 'locator': '//*[@text="行情" and @resource-id="com.xueqiu.android:id/tab_name"]', 'action': 'click'}]
        steps = datas[func]
        self.action(steps,value)

    def action(self, steps, value=""):
        # step={'by': 'id', 'locator': 'com.xueqiu.android:id/post_status', 'action': 'click'}
        # step={'by': 'xpath', 'locator': '//*[@text="行情" and @resource-id="com.xueqiu.android:id/tab_name"]', 'action': 'click'}
        for step in steps:
            sleep(1)
            if step['action'] == 'click':
                self.find(step['by'], step['locator']).click()
            elif step['action'] == 'sendkey':
                self.find(step['by'], step['locator']).clear()
                self.find(step['by'], step['locator']).send_keys(value)
