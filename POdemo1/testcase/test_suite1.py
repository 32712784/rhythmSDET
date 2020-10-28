# coding=utf-8
from time import sleep

import pytest as pytest

from rhythmSDET.POdemo1.page.main_page import MainPage

class TestDomo():
    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize("username,id,phone",[["测试00008","test00008","13011111118"]])
    def test_addmember(self,username,id,phone):
        # username = "测试00008"
        # id = "test00008"
        # phone = "13011111118"
        #按照下面方式，会执行两遍goto_AddMember方法，导致进入联系人列表后还会点一次添加联系人，就报错了
        # self.main.goto_AddMember().add_member(username,id,phone)
        # self.main.goto_AddMember().get_member()

        #self.main.goto_AddMember()初始化一遍后，返回的是AddMemberPage类的实例化对象，后续就直接使用此类下面的方法了。
        addmember = self.main.goto_AddMember()
        addmember.add_member(username,id,phone)
        titles = addmember.get_member()
        assert  username in titles


        #尝试首页和联系人页来回切换
        # addmember = self.main.goto_AddMember()
        # sleep(1)
        # addmember.goto_main_page()
        # sleep(1)
        # importcontans = self.main.goto_Import()
        # sleep(1)
        # importcontans.goto_main_page()


