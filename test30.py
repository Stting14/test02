# -*- coding: UTF-8 -*-



import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1501115871@qq.com"    #用户名
mail_pass="wdqnftnzelfofhae"   #校验码


sender = "1501115871@qq.com"
#receivers = ['495450092@qq.com']# 接收邮件
receivers = '1501115871@qq.com'

message = MIMEText('Python ...', 'plain', 'utf-8')
message['From'] = sender
message['To'] =  receivers

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 465)    # 465 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

 
