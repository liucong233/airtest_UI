import logging

import yaml
from airtest.core.api import *
from public.tool import Tools
import time
from airtest.utils.logger import get_logger
from public.webdriver import AutoWeb

phone_flag = True


class App:
    logger = get_logger('log')
    config = yaml.safe_load(open('../config/device.yaml', 'r', encoding='utf-8'))
    driver = AutoWeb()

    @classmethod
    def start(cls, project):
        config = cls.config[project]
        # app配置
        if phone_flag:
            # 连接手机
            # dev = connect_device(
            #     "{}://127.0.0.1:5037/{}?cap_method=JAVACAP".format(config['platformName'], config['deviceName']))
            dev = connect_device(
                "Android://127.0.0.1:5037/192.168.10.39:1314?cap_method=javacap&touch_method=adb")
            dev.wake()
            # 唤醒手机
            # 安装app
            # try:
            #     dev.check_app(channel_config['appPackage'])
            # except Exception:
            #     cls.logger.info('-----------------正在安装{}渠道app，请稍候...-----------------'.format(channel))
            # install('../app_package/v{}/hlsg3_v{}_{}.apk'.format(version, version, channel))
            poco = Tools(use_airtest_input=True, screenshot_each_action=False)
            # install('../app_package/v{}/hlsg3_v{}_{}.apk'.format(version, version, channel))
            cls.logger.info('-----------------请稍候...-----------------')
            # 启动app
            stop_app(config['appPackage'])
            start_app(config['appPackage'])
            # stop_app(config['appPackage'])
            return poco

        # web配置
        cls.logger.info('-----------------正在启动web，请稍候...-----------------')
        url = config['url']
        cls.driver.maximize_window()
        cls.driver.get(url)
        return cls.driver

    @classmethod
    def quit(cls):
        time.sleep(10)
        cls.driver.quit()
