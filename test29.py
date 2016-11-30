# -*- coding: UTF-8 -*-

# Filename : test29.py
# author by : STT


import smtplib
from email.mine.text import MIMEText
from email.header import Header

sender='from@runoob.com'
receivers=['1501115871@qq.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
messege=MIMEText('Python 邮件发送测试。。。','plain','utf-8')
messege['From']=Header('菜鸟教程','utf-8')
messege['To']=Header('测试','utf-8')

subject='Python SMTP邮件测试'
messege['Subject']=Header(subject,'utf-8')

try:
    smtpa=smtplib.SMTP('localhost')
    smtpa.sendmail(sender,receivers,messege.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')
