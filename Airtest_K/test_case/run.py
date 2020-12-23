import pytest
import os
import yaml
from public.email import Email
from public.report import get_report, zip_file

if __name__ == "__main__":
    config = yaml.safe_load(open('../config/device.yaml', 'r', encoding='utf-8'))["hlsg3"]

    # # 删除上次测试数据
    # os.system(r'del /s /q ..\report\data\*.*')
    # # 生成测试数据
    # # pytest.main(['-s', '-q', '--alluredir', '../report/data', '-W ignore::DeprecationWarning'])
    # filename = "test_demo.py"
    # # filepath1 = "./{}".format(filename)
    # pytest.main(['-s', '-q', '--alluredir', '../report/data', '-W ignore::DeprecationWarning', filename])

    # 生成测试报告
    os.system('allure generate ../report/data -o ../report/html --clean')


    # # 获取测试报告
    # get_report()
    # # 打包测试报告截图
    # zip_file(config['zip']['dir_path'], config['zip']['out_filename'])
    # # 发送邮件
    email = Email()
    email.send_email()


