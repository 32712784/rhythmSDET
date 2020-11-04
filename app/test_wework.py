# coding=utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
import pytest

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
        # 跳过服务安装初始化
        caps["skipServerInstallation"] = "True"
        # 中文输入内容时，需要提前设置
        caps["unicodeKeyBoard"] = "True"
        caps["resetKeyBoard"] = "True"
        # # 设置全局idle等待时间为0
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
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

    def test_add_contact(self):
        name = "测试00004"
        gender = "男"
        phonenum = "13500000001"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # sleep(2)
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == result

    @pytest.mark.parametrize("username",[("测试00005"),("测试00006"),("测试00009"),("test")])
    def test_del_contact(self,username):
        # username='测试00006'
        # 点击通讯率
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击右上角编辑图标
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gup").click()
        # 点击其中一个联系人
        WebDriverWait(self.driver,5).until(lambda x: x.find_element(MobileBy.XPATH, f"//*[@text='{username}']"))
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{username}']").click()
        # 点击删除
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # 点击确定
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        # 断言等待用户名消失
        WebDriverWait(self.driver,10).until_not(lambda x : x.find_element(MobileBy.XPATH, f"//*[@text='{username}']"))
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guk").click()

