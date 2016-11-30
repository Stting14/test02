# -*- coding: UTF-8 -*-

# Filename : test11.py
# author by : STT

#通过用户输入数字计算阶乘
num=int(input('请输入一个数字：'))
factorial=1

#查看数字是负数，零活或正数
if num<1:
    print('负数没有阶乘')
elif num==0:
    print('0的阶乘为1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print('%d的阶乘为 %d' % (num,factorial))
