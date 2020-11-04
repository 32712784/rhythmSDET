# coding=utf-8
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from rhythmSDET.app.page.address_book_page import AddressBookPage
from rhythmSDET.app.page.base_page import BasePage
from rhythmSDET.app.page.main_page import MainPage


class App(BasePage):
    def start(self):
        # 新开的driver
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "ctyAutotest"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
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
            # 初始化MobileBy，传给self.by
            self.by = MobileBy
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def quit_app(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)

    # def goto_member_invite_menu(self):
    #     return AddressBookPage(self.driver)