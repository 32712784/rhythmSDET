# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from rhythmSDET.app.page.base_page import BasePage


class AddressSearchPage(BasePage):
    # 搜索联系人页面进行搜索并返回搜索结果数量
    def search_contact_and_get_result(self, name):
        self.find(MobileBy.ID, "com.tencent.wework:id/fk1").send_keys(name)
        search_count = len(self.finds(MobileBy.XPATH,f"//*[@class='android.widget.ListView']//*[@text='{name}']"))
        return search_count

    # 从搜索页面返回到通讯录页面
    def back_address_book_page(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/gu_").click()
        from rhythmSDET.app.page.address_book_page import AddressBookPage
        return AddressBookPage(self.driver)
