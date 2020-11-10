# coding=utf-8
import yaml

from rhythmSDET.CustomerFrame.page.main_page import MainPage


class TestDemo():
    def setup(self):
        self.main = MainPage()
        pass

    def teardown(self):
        self.main.quit_app()
        pass

    def test_search(self):
        self.main.goto_market_page().goto_search_page().search("阿里巴巴","BABA")
        pass

    # def test_parse_yaml(self):
    #     path = r"D:\Python3_workspace\rhythmSDET\CustomerFrame\page\main_page.yaml"
    #     with open("./../page/main_page.yaml") as f:
    #         data = yaml.load(f)
    #         print(data['goto_market_page'])