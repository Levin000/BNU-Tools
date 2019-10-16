#!/usr/bin/env python3
#-*-coding:utf-8-*- 

import requests
import socket
import os

class logout(object):
    header = {
        'Host': '172.16.202.201:801',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh,zh-CN;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://172.16.202.201:801/srun_portal_pc.php?ac_id=1&',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '106',
        'Connection': 'keep-alive',
        'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYf0isl5GavYmBpS5EMYCNKzR6wbUTXsdad%252B5i7K5PJYlrFhUEp6fDmgPDAll59HPpSAPSZbqvWLewtKkBcdJX8vwKLPM20Aq%252BZXsCEnpWQjtWjI7QiDVC49BUCiX%252Fn097vUMmP269bVRPxukYW%252FqVscMCfm000troPSyKzS0WDGoL42RP2t7ZrDOviMV0jow3cbqdiJJ4dWin16qsDay250Zak47ANyqNyu66mdDzwZMHTwdtqUvY6jsU9V90I9o; language=en',
        'Upgrade-Insecure-Requests': '1'
    }
    paras = {
        'action': 'login',
        'ac_id': '1',
        'user_ip': '',
        'nas_ip': '',
        'user_mac': '',
        'url': '',
        'username': '',
        'password': '',
        'save_me': '1'
    }
    logout_paras = {
        'action': 'auto_logout',
        'info': '',
        'user_ip': ''
    }
    url = 'http://172.16.202.201:803/srun_portal_pc.php?ac_id=1&'
    ip = '',
    
    def __init__(self):
        """
        初始化学号/认证密码信息
        """
        dirname, filename = os.path.split(os.path.abspath(__file__))
        with open(os.path.join(dirname,'bnu.network.userinfo'),'r+') as f:
            line = f.readline()
            while line:
                text,content = line.split(':')
                if text.strip() == 'studentID':
                    self.username = content.strip()
                elif text.strip() == 'password':
                    self.password = content.strip()
                line = f.readline()
    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        print(ip)
        return ip

    def update_cookies(self):
        resp = requests.post(url=self.url, data=self.paras)
        self.header['Cookie'] = resp.cookies.get('login')
        print('Cookies updated!')

    def logout(self):
        self.update_cookies()
        self.logout_paras['user_ip'] = self.get_host_ip()
        resp = requests.post(
            url=self.url, data=self.logout_paras, headers=self.header)
        if resp.ok:
            print('本机成功退出登录')
if __name__ == '__main__':
    app = logout()
    app.logout()

