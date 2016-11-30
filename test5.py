# -*- coding: UTF-8 -*-

# Filename : test5.py
# author by : STT

#用户输入
x=input('输入x的值：')
y=input('输入y的值：')

#创建临时变量并交换
#temp=x
#x=y
#y=temp

#print('交换后x的值为：{}'.format(x))
#print('交换后y的值为：{}'.format(y))


#不使用临时变量
x,y=y,x
print('交换后x的值为：{}'.format(x))
print('交换后y的值为：{}'.format(y))
