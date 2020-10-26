# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def add_member(self,username,id,phone):
        """
        #添加联系人
        :return:
        """

        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.NAME, "acctid").send_keys(id)
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR,".qui_btn.ww_btn.js_btn_save").click()
        return True

    def get_member(self):
        """
        获取联系人列表
        :return: title_list
        """
        name_elements = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        #列表推导式
        title_list = [element.get_attribute("title") for element in name_elements]

        # for element in name_elements:
        #     title_list.append(element.get_attribute("title"))
        return title_list

