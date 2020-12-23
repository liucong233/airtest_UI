import os
import time
import zipfile

from public.webdriver import AutoWeb
from test_case.launch import App


def zip_file(dir_path, out_filename):
    testcase_zip = zipfile.ZipFile(out_filename, 'w', zipfile.ZIP_DEFLATED)
    for path, _, file_names in os.walk(dir_path):
        for filename in file_names:
            file_path = os.path.join(path, filename)
            if 'image' not in file_path and 'zip' not in file_path:
                testcase_zip.write(file_path)
    testcase_zip.close()


def get_report():
    # 打开测试报告
    config = App.config
    # 获取工程名
    project_name = os.getcwd().split('\\')[-2]
    report_url = 'http://localhost:63342/' + project_name + config['report_url']
    driver = AutoWeb()
    driver.maximize_window()
    driver.get(report_url)
    # 报告修改为中文
    driver.find_element_by_class_name('button_inverse').click()
    driver.find_element_by_xpath("//*[@data-id='zh']").click()
    time.sleep(3)
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # 检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        file_path = "..\\report\\image\\" + directory_time
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    except BaseException as msg:
        App.logger.error("新建目录失败：%s" % msg)
    profile = '..\\report\\image\\{}\\a_profile.png'.format(directory_time)
    func = '..\\report\\image\\{}\\func.png'.format(directory_time)
    driver.save_screenshot(profile)
    driver.find_element_by_xpath("//*[@data-tooltip='功能']").click()
    time.sleep(3)
    driver.save_screenshot(func)
