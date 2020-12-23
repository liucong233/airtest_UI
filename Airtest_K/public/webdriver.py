import logging

from airtest.utils.logger import get_logger
# from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from airtest_selenium.proxy import WebChrome


class AutoWeb(WebChrome):
    logger = get_logger('selenium')
    logger.setLevel(logging.INFO)
    max_time = 10

    def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None):
        super(AutoWeb, self).__init__(chrome_options=chrome_options, executable_path=executable_path,
                                      port=port, options=options, service_args=service_args,
                                      service_log_path=service_log_path, desired_capabilities=desired_capabilities)

    def find_element_by_id(self, el):
        try:
            self.logger.info("---------->正在定位{}".format(el))
            element = WebDriverWait(self, self.max_time).until(EC.visibility_of_element_located((By.ID, el)))
        except Exception:
            self.logger.error("---------->定位失败:{}".format(el))
            raise
        else:
            self.logger.info("---------->定位成功:{}".format(el))
            return element

    def find_elements_by_id(self, el):
        try:
            self.logger.info("---------->正在定位{}".format(el))
            elements = WebDriverWait(self, self.max_time).until(
                EC.visibility_of_all_elements_located((By.ID, el)))
        except Exception:
            self.logger.error("{}定位失败".format(el))
            raise
        else:
            self.logger.info("---------->定位成功:{}".format(el))
            return elements

    def find_element_by_class_name(self, el):
        try:
            self.logger.info("---------->正在定位{}".format(el))
            element = WebDriverWait(self, self.max_time).until(EC.visibility_of_element_located((By.CLASS_NAME, el)))
        except Exception:
            self.logger.error("---------->定位失败:{}".format(el))
            raise
        else:
            self.logger.info("---------->定位成功:{}".format(el))
            return element

    def find_elements_by_class_name(self, el):
        try:
            self.logger.info("---------->正在定位{}".format(el))
            elements = WebDriverWait(self, self.max_time).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, el)))
        except Exception:
            self.logger.error("{}定位失败".format(el))
            raise
        else:
            self.logger.info("---------->定位成功:{}".format(el))
            return elements

    def find_element_by_xpath(self, el):
        try:
            self.logger.info("---------->正在定位{}".format(el))
            element = WebDriverWait(self, self.max_time).until(EC.visibility_of_element_located((By.XPATH, el)))
        except Exception:
            self.logger.error("---------->定位失败:{}".format(el))
            raise
        else:
            self.logger.info("---------->定位成功:{}".format(el))
            return element

    def find_elements_by_xpath(self, el):
        try:
            self.logger.info("---------->正在定位{}".format(el))
            elements = WebDriverWait(self, self.max_time).until(
                EC.visibility_of_all_elements_located((By.XPATH, el)))
        except Exception:
            self.logger.error("{}定位失败".format(el))
            raise
        else:
            self.logger.indo("---------->定位成功:{}".format(el))
            return elements
