import requests

from test_case.launch import App
import allure
from airtest.core.api import *

img_dir = '../case_img/test_demo'
logger = App.logger


@allure.feature('测试test_demo')
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.web = App.start('test_project')

    @allure.title("测试登录")
    def test_login_on(self):
        with allure.step("输入用户名"):
            sleep(3)
            self.web.find_element_by_xpath("//*[@type='text']").send_keys('zwq')
        with allure.step("输入密码"):
            sleep(3)
            self.web.find_element_by_xpath("//*[@type='password']").send_keys('situ1234')
        with allure.step("点击登录"):
            self.web.airtest_touch(Template('{}/login_on.png'.format(img_dir)))

    @allure.title("测试退出")
    def test_log_out(self):
        pass

    @classmethod
    def teardown_class(cls):
        App.quit()
