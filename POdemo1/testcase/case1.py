# coding=utf-8
from rhythmSDET.POdemo1.page.main_page import MainPage

class TestDomo:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "测试00003"
        id = "test00003"
        phone = "13011111113"
        #按照下面方式，会执行两遍goto_AddMember方法，导致进入联系人列表后还会点一次添加联系人，就报错了
        # self.main.goto_AddMember().add_member(username,id,phone)
        # self.main.goto_AddMember().get_member()

        #self.main.goto_AddMember()初始化一遍后，返回的是AddMemberPage类的实例化对象，后续就直接使用此类下面的方法了。
        addmember = self.main.goto_AddMember()
        print(addmember)
        addmember.add_member(username,id,phone)
        titles = addmember.get_member()
        assert  username in titles


