# coding=utf8
import requests

from test_case.launch import App
import allure
from airtest.core.api import *

img_dir = '../case_img/test_demo'
logger = App.logger


@allure.feature('测试test_demo2')
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.poco = App.start('test_project')

    @allure.title("测试登录2")
    def test_login_on(self):
        pass

    @allure.title("测试企业微信demo")
    def test_wx(self):
        self.poco(text='微信登录').click()

    @classmethod
    def teardown_class(cls):
        App.quit()
