# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from rhythmSDET.CustomerFrame.page.base_page import BasePage
from rhythmSDET.CustomerFrame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        # 点击笔图标，模拟黑名单
        self.parse_yaml("./../page/main_page.yaml","goto_market_page")
        # self.find(MobileBy.ID,"com.xueqiu.android:id/post_status").click()
        # #点击行情tab
        # self.find(MobileBy.XPATH,"//*[@text='行情' and @resource-id='com.xueqiu.android:id/tab_name']").click()
        return MarketPage(self.driver)
