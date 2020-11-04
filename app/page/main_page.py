# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from rhythmSDET.app.page.address_book_page import AddressBookPage
from rhythmSDET.app.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address_book(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressBookPage(self.driver)