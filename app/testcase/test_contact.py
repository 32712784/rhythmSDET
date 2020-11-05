# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
import pytest
from rhythmSDET.app.page.app import App


class TestContact():
    def setup_class(self):
        self.app = App()
        self.main = self.app.start()

    def teardown_class(self):
        self.main.quit_app()

    @pytest.mark.parametrize("name,sex,phone",[("测试00003","男","13800010003"),("测试00004","男","13800010004"),("测试00005","男","13800010005"),("测试00006","男","13800010006")])
    def test_add_contact(self,name,sex,phone):
        # name="测试00003"
        # sex = "男"
        # phone = "13800010003"
        # 添加成员后，跳转到member_invite_menu页面
        member_invite_menu = self.main.goto_main().goto_address_book().goto_member_invite_menu().goto_contact_add().add_contact_and_goto_invite_menu(
            name, sex, phone)
        # 捕获toast
        result=member_invite_menu.get_toast()
        assert result == "添加成功"
        print(result)
        # 点击返回，再进入搜索页面，进行搜索，并返回搜索结果
        search_page = member_invite_menu.back_address_book_page().goto_address_search_page()
        search_count = search_page.search_contact_and_get_result(name)
        assert search_count == 1
        print(search_count)
        # 重新返回到通讯录页面
        search_page.back_address_book_page()


    def test_del_contact(self):
        name = "测试00005"
        #通讯录页面
        goto_address = self.main.goto_main().goto_address_book()
        #搜索联系人页面
        search_page = goto_address.goto_address_search_page()
        #进入搜索页面，搜索并得到结果
        before = search_page.search_contact_and_get_result(name)
        print(before)
        #从搜索页面返回到联系人页面
        back_address = search_page.back_address_book_page()
        #删除联系人操作
        back_address.delete_contact(name)
        # 再从联系人页面进入搜索页面进行搜索
        search_page = back_address.goto_address_search_page()
        after = search_page.search_contact_and_get_result(name)
        print(after)
        assert after==before-1
        # 重新返回到通讯录页面
        search_page.back_address_book_page()




