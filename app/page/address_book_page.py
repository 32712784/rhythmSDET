# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from rhythmSDET.app.page.address_search_page import AddressSearchPage
from rhythmSDET.app.page.base_page import BasePage
from rhythmSDET.app.page.member_invite_menu_page import MemberInviteMenuPage


class AddressBookPage(BasePage):
    # 点击添加成员跳转到中转页面
    def goto_member_invite_menu(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInviteMenuPage(self.driver)

    # 点击搜索按钮跳转到搜索页面
    def goto_address_search_page(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/guu").click()
        return AddressSearchPage(self.driver)

    # 删除联系人
    def delete_contact(self,username):
        # 点击右上角编辑图标
        self.find(MobileBy.ID, "com.tencent.wework:id/gup").click()
        # 点击对应名字的联系人
        self.find(MobileBy.XPATH, f"//*[@text='{username}']").click()
        # 点击删除
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # 点击确定
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        # 等待用户名消失，然后点击右上角的X
        self.wait_element_invisible(MobileBy.XPATH, f"//*[@text='{username}']")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guk").click()