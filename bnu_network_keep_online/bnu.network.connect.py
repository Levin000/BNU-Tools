
#!/usr/bin/env python3
#-*-coding:utf-8-*- 

import requests
import os
import socket 
from time import sleep

class login(object):
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
    url = 'http://172.16.202.201:803/srun_portal_pc.php?ac_id=1&'
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
                    self.paras['username'] = content.strip()
                elif text.strip() == 'password':
                    self.paras['password'] = content.strip()
                line = f.readline()
            
    def update_cookies(self):
        resp = requests.post(url=self.url, data=self.paras)
        self.header['Cookie'] = resp.cookies.get('login')
        print('Cookies updated!')
    
    def login(self):
        self.update_cookies()
        resp = requests.post(url=self.url,data=self.paras,headers=self.header)
        if resp.ok:
            if '终端数已达上限，请登录自服务主动下线' in resp.text:
                print('终端数已达上限，请登录自服务主动下线')
            else:
                print('connect the BNU internet success!')
        else:
            print('connect failed! please check internet condition.')
            
def isNetOK(testserver): 
    s=socket.socket() 
    s.settimeout(3) 
    try: 
        status = s.connect_ex(testserver) 
        if status == 0: 
            s.close() 
            return True 
        else: 
            return False 
    except Exception as e: 
        return False 
def isNetConnected(testserver=('www.baidu.com',443)): 
    isOK = isNetOK(testserver) 
    return isOK 
    

if __name__ == '__main__':
    app = login()
    app.login()
    
    while True:
        isOK = isNetConnected() 
        if isOK:
            print('Network is Connected!')
            sleep(60)
        else:
            print("网络断开，尝试重新链接···")
            
            app.login()
            print('Network is Connected!')
            sleep(300)
