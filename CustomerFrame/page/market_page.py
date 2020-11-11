# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from rhythmSDET.CustomerFrame.page.base_page import BasePage
from rhythmSDET.CustomerFrame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search_page(self):
        self.parse_yaml("./../page/market_page.yaml","goto_search_page")
        # self.find(MobileBy.ID, "com.xueqiu.android:id/action_search").click()
        return SearchPage(self.driver)
