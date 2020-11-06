# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy

from rhythmSDET.app.page.base_page import BasePage
# from rhythmSDET.app.page.member_invite_menu_page import MemberInviteMenuPage


class ContactAddPage(BasePage):
    def add_contact_and_goto_invite_menu(self,name,sex,phone):
        self.log().info(f"添加成员：姓名【{name}】，性别：【{sex}】，电话：【{phone}】")
        # 姓名
        self.find(MobileBy.ID, "com.tencent.wework:id/au0").send_keys(name)
        # 性别选择
        self.find(MobileBy.ID, "com.tencent.wework:id/dux").click()
        self.find(MobileBy.XPATH, f"//*[@resource-id='com.tencent.wework:id/b9z']//*[@text='{sex}']").click()
        # 电话
        self.find(MobileBy.ID, "com.tencent.wework:id/eq7").send_keys(phone)
        # 保存
        self.find(MobileBy.ID, "com.tencent.wework:id/gur").click()
        from rhythmSDET.app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)