# coding=utf-8
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from rhythmSDET.CustomerFrame.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, stock_name_or_code, stockCode):
        # 通过股票名或代码搜索
        self.parse_yaml("./../page/search_page.yaml","search",stock_name_or_code)
        # self.find(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(stock_name_or_code)
        # sleep(1)
        # self.find(MobileBy.ID,"com.xueqiu.android:id/search_input_text").click()
        self.find(MobileBy.XPATH,f"//*[@text='{stockCode}']").click()
        # 根据股票代码，确认相应股票价格
        current_price = self.find(MobileBy.XPATH,f"//*[@text='{stockCode}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(current_price)
        return current_price
