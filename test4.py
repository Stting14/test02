# -*- coding: UTF-8 -*-

# Filename : test4.py
# author by : STT

#用户输入摄氏温度

#接收用户输入
C=float(input('输入摄氏温度：'))
#计算华氏温度
F=(C*1.8)+32
print('%0.1f 摄氏温度转化为华氏温度为 %0.1f' % (C,F))


#接收用户输入
F=float(input('请输入华氏温度：'))
#计算摄氏温度
C=(F-32)/1.8
print('%0.1f 华氏温度转化为摄氏温度为 %0.1f' %(F,C))
