# coding=gbk
import logging
import mimetypes
import os
import smtplib
import time
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import datetime

import requests
from airtest.utils.logger import get_logger

import yaml

send_time = datetime.datetime.today().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}'). \
    format(y='年', m='月', d='日', h='时', f='分')


class Email(object):
    global send_time
    logger = get_logger('Email')
    logger.setLevel(logging.INFO)

    def __init__(self):
        self.config = yaml.safe_load(open('../config/email.yaml', 'r'))
        self.smtp_server = self.config['Email']['smtp_server']
        self.username = self.config['Email']['username']
        self.password = self.config['Email']['password']
        self.file_path = self.config['Email']['file_path']
        self.sender = self.config['Email']['sender']
        self.receivers = self.config['Email']['receivers']
        self.addr_from = self.config['Email']['from']
        self.addr_to = self.config['Email']['to']

    @staticmethod
    def get_image_url(images_path):
        url = 'http://t-app.moego.net/common/upload?__debug__=1'
        images_url = []
        for dir_path, _, files_name in os.walk(images_path):
            for file_name in files_name:
                image_path = os.path.join(dir_path, file_name)
                params = {
                    'type': 0,
                    'picture_type': 3,
                }
                files = {
                    'file': open(image_path, 'rb'),
                }

                req = requests.post(url=url, data=params, files=files).json()
                image_url = req['data']['path']
                images_url.append(image_url)
        return images_url

    # 设置邮件正文
    def set_content(self, attach_zip):
        msg = MIMEMultipart()
        # msg.attach(MIMEText("{}的测试报告见附件".format(time), 'plain', 'utf-8'))  # 邮件正文
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        images_path = '..\\report\\image\\{}'.format(directory_time)
        images_url = self.get_image_url(images_path)
        self.logger.info(images_url)
        content = '<h3>{}的测试结果见下图，更多详情见附件html/index.html</h3>'.format(send_time)
        images = ''
        for image_url in images_url:
            image = '<p><img width=1500 height=700 src="{}"></p>'.format(image_url)
            images += image
        email_html = '<html><body>' + content + images + '</body></html>'
        msg.attach(MIMEText(email_html, 'html', 'utf-8'))
        msg['From'] = self.addr_from  # 发送邮件的地址
        msg['To'] = self.addr_to  # 接收邮件的地址
        subject = "{}的SDK测试报告".format(send_time)  # 邮件标题
        msg['Subject'] = subject
        msg.attach(attach_zip)
        return msg

    # 设置附件
    def set_attach(self):
        data = open(self.file_path, 'rb')
        ctype, encoding = mimetypes.guess_type(self.file_path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        attach_zip = MIMEBase(maintype, subtype)
        attach_zip.set_payload(data.read())
        data.close()
        encoders.encode_base64(attach_zip)  # 把附件编码
        # 修改附件名称
        filename = "{}-测试报告.zip".format(send_time)
        attach_zip.add_header('Content-Disposition', 'attachment', filename=filename)
        return attach_zip

    # 发送邮件
    def send_email(self):
        try:
            server = smtplib.SMTP(self.smtp_server, 25)
            server.login(self.username, self.password)
            attach_zip = self.set_attach()
            msg = self.set_content(attach_zip)
            server.sendmail(self.sender, self.receivers, msg.as_string())
            server.quit()
            self.logger.info('---------->发送邮件成功')
        except Exception as err:
            self.logger.info('---------->发送邮件失败')
            self.logger.info(err)
