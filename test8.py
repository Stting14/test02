# -*- coding: UTF-8 -*-

# Filename : test8.py
# author by : STT

#python 判断基数和偶数

#如果是偶数除以2余数为0
#如果余数为1为基数

num=int(input('请输入一个数字：'))
if (num % 2)==0:
    print('{}是偶数'.format(num))
    #print('%s是ou数'% num)
else:
    print('{0}是基数'.format(num))
