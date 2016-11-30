import urllib.request
import re

class login():
    
    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd

    def hwqlogin(self):
        url ='http://xxx.xx.xx.xxx:11011/TransfServices/appservice/user/cmp_uinfo.do?'
        #user='xxxx'
        #passwd='xxxx'

        #response = urllib.request.urlopen(url+"key="+user+"&password="+passwd)
        response = urllib.request.urlopen(url+"key="+self.user+"&password="+self.passwd)
        html=response.read()
        html=html.decode('utf-8')
        print(html)

        patten=re.compile(r'"flag":"(.*?)"',re.S)
        lists=re.findall(patten,str(html))
        print(lists)

        for i in lists:
            if int(i)==1:
                print('登录成功')
            elif int(i)==-6:
                print('输入错误')
            else:
                print('Fause')


if __name__=='__main__':
    #f=open('D:/test.txt','r')
    user='xxxxxxx'
    passwd='xxxxxx'
    login(user,passwd).hwqlogin()



















