# coding=utf-8
from logging import exception

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethod:
    base_url = ""

    def __init__(self,driver: WebDriver=None):
        #没传driver变量，默认为None，说明是新开的浏览器，否则复用跳转时传入的driver
        if driver == None:
            options=Options()
            options.debugger_address="localhost:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        #base_url打开页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self,by,locator):
        if by.lower()=="css":
            return self.driver.find_element(By.CSS_SELECTOR,locator)
        if by.lower()=="id":
            return self.driver.find_element(By.ID, locator)
        if by.lower()=="xpath":
            return self.driver.find_element(By.XPATH, locator)
        if by.lower()=="name":
            return self.driver.find_element(By.NAME, locator)
        if by.lower()=="linktext":
            return self.driver.find_element(By.LINK_TEXT, locator)
        pass

    def finds(self,by,locator):
        if by.lower()=="css":
            return self.driver.find_elements(By.CSS_SELECTOR,locator)
        if by.lower()=="id":
            return self.driver.find_elements(By.ID, locator)
        if by.lower()=="xpath":
            return self.driver.find_elements(By.XPATH, locator)
        if by.lower()=="name":
            return self.driver.find_elements(By.NAME, locator)
        if by.lower()=="linktext":
            return self.driver.find_elements(By.LINK_TEXT, locator)
        pass

    def wait_for_visible(self,*locator,timeout=10):
        """
         #等待元素显示
        :param locator:
        :param timeout:
        :return:
        """
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        return element


    def wait_for_input_success(self,*locator,value,timeout=10):
        """
        等待内容输入成功，默认重试10秒
        :param locator:
        :param value:
        :param timeout:
        :return:
        """
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).send_keys(value)
                return True
            except:
                return False
        try:
            WebDriverWait(self.driver,timeout,0.5).until(wait_for_next)
            return True
        except:
            return False

