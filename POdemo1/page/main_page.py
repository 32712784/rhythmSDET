# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from rhythmSDET.POdemo1.page.add_member_page import AddMemberPage
from rhythmSDET.POdemo1.base.base_method import BaseMethod

class MainPage(BaseMethod):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address="localhost:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.implicitly_wait(5)

    def goto_AddMember(self):
        self.find("css",".ww_indexImg.ww_indexImg_AddMember").click()
        # self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg.ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)

    def goto_Import(self):
        self.find("css",".ww_indexImg.ww_indexImg_Import").click()
        return AddMemberPage(self.driver)