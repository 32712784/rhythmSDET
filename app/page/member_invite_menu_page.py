# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from rhythmSDET.app.page.base_page import BasePage
from rhythmSDET.app.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    # 中转页点击手动输入添加
    def goto_contact_add(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/c7g").click()
        return ContactAddPage(self.driver)

    # 获取Toast文本内容
    def get_toast(self):
        return self.get_toast_text()

    # 点击返回按钮到通讯录页面
    def back_address_book_page(self):
        # 添加联系人成功后，会有Toast，等Toast消失后再操作，否则会失败
        self.wait_element_invisible(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        self.find(MobileBy.ID, "com.tencent.wework:id/gu_").click()
        from rhythmSDET.app.page.address_book_page import AddressBookPage
        return AddressBookPage(self.driver)
