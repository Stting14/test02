#-*- coding:utf-8 -*-
import urllib
import re

class login():
    def __init__(self,user,passwd):
        self.user = user
        self.passwd = passwd
        
        
    def hwqLogin(self):
        url='http://120.77.65.142:11011/TransfServices/appservice/user/cmp_uinfo.do?'
        response = urllib.urlopen(url+"key="+self.user+"&password="+self.passwd)
        html=response.read()
        html=html.decode('utf-8')
        print html

        pattern = re.compile(r'"flag":"(.*?)"}',re.S)
        lists = re.findall(pattern,str(html))
        for i in lists:
            if int(i)== -2:
                print "用户名或密码错误。"
            elif int(i) == 1:
                print "登陆成功."
            else:
                print "False."
        
                
if __name__ == "__main__":       
    user = "18613187321"
    passwd = "123456789"
    login(user,passwd).hwqLogin()