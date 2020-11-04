# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by,locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by,locator)

    def wait_element_visibility(self,by,locator):
        WebDriverWait(self.driver, 5).until(lambda x : x.find_element(by, locator))
        return self.find(by, locator)

    def wait_element_invisible(self,by,locator):
        WebDriverWait(self.driver, 5).until_not(lambda x : x.find_element(by, locator))

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

