# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFile():
    def test_upfile(self):
        """
        文件上传验证
        通过文件上传按钮的input标签进行文件上传
        :return:
        """
        options = Options()
        # options.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://10.5.11.4:9110/wf/appservice/ApprovePage/Approve?frommail=1&mode=2&oid=8eba74f5-b41d-eb11-b2ce-00155d0a084b")
        self.driver.find_element(By.NAME,"user").send_keys("admin")
        self.driver.find_element(By.NAME,"pwd").send_keys("1")
        self.driver.find_element(By.NAME,"submit").click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"file")))
        # 通过定位上传按钮的input标签，输入附件全路径，可以直接上传附件
        self.driver.find_element(By.CSS_SELECTOR,".webuploader-element-invisible").send_keys(r"C:\Users\xshj\Desktop\用户并发组合场景结果20200705.xlsx")
        sleep(3)