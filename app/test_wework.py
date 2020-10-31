# coding=utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "rhythmTest"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 此参数设置后，执行完用例不会关闭APP
        caps["dontStopAppOnReset"] = True
        # 不加此参数，会需要登录
        caps["noReset"] = "True"
        # 跳过设备初始化，加快执行速度
        caps["skipDeviceInitialization"] = "True"
        # 中文输入内容时，需要提前设置
        caps["unicodeKeyBoard"] = "True"
        caps["resetKeyBoard"] = "True"
        # # 设置全局idle等待时间为0
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        # 点击工作台
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 自动滚动屏幕点击进入打卡
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='打卡']").click()
        # 设置idle等待时间为0(局部)
        # self.driver.update_settings({"waitForIdleTimeout":0})
        # 点击外出打卡
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 点击打卡
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # 断言方式1
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        # 通过显示等待断言2
        WebDriverWait(self.driver,10).until(lambda x : "外出打卡成功" in x.page_source)
        self.driver.back()

    def test_demo(self):
        # el1 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.TextView")
        # el1.click()
        # el2 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[10]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
        # el2.click()
        # el3 = self.driver.find_element_by_id("com.tencent.wework:id/ghc")
        # el3.click()

        # accessibility_id就是元素的content-desc，xxxx输入content-desc的值
        self.driver.find_element_by_accessibility_id("xxxx")
        pass

