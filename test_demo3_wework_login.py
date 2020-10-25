# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address="localhost:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        # self.driver.quit()
        pass

    def test_test1demo(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text(u"新闻").click()

    def test_cookie(self):
        cookie = self.driver.get_cookies()
        print(cookie)

    def test_openwx(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853322238872'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325054170011'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853322238872'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'lndOpFHrhfOInfHN78g0j9-sCL-SR9hUAH3zpXVoxipEh73Di3_86FLjOz5MAOnY'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2630213'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'cL2J3DbrBjxOUO6x1MRoZs6GAf0_Un9UADhXaBkM6hqBT6a_-GQuEXVeDq2gRHa63z_Ua973xqXUKeKMPgPBdY1e09xA3qt2VNq1RyFA5lkD-vKYEh02THS-7cZXDf-OrzlMn7Q4qzxHZsPOcdf0sg3xPXn2MoZeaePboDQ5NNRxfxjqGOrq46UruhkWp5c_7T2xHR8uEhrFjhgLJbrYy0EFuDG2VMdAdkHTiVuvLMiGTfGDn0YpF9BUzHXAsdy8zPPHRQlT1C8MvCBcEtC9IA'},
            {'domain': '.qq.com', 'expiry': 1666710122, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1962092762.1603636511'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1603638112'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '38619954472109112'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635172508, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1868106527, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_32712784'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '32712784'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'b37ebb6cc413cee2da0b309ec8619e6af8b9acb11f68cc885aaacfc1edfb515d'},
            {'domain': '.qq.com', 'expiry': 1603724522, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1636676765.1603636511'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603668044, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '7l2ia8m'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '8146448384'},
            {'domain': '.qq.com', 'expiry': 1865344159, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'af2c01cf4d04b206'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635174111, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1603636510'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '5959765250'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483651, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'ZZb8kXChQ6'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606230233, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

