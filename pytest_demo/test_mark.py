# coding=utf8
import pytest

class TestMark:
    # @pytest.mark.login
    def test_login(self):
        print("登陆成功")

    @pytest.mark.login
    def test_login2(self):
        print("登陆成功2")

    @pytest.mark.search
    def test_search(self):
        print("搜索成功")

    @pytest.mark.search
    def test_search1(self):
        print("搜索成功2")
