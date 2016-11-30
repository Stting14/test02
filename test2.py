# _*_ coding: UTF-8 _*_

#FileName : test2.py

# author by: STT

#计算三角形面积

#请输入边长

a=float(input('请输入一遍的长度：'))
b=float(input('请输入一遍的长度：'))
c=float(input('请输入一遍的长度：'))

#计算半周长
s=(a+b+c)/2

#计算面积

area=(s*(s-a)*(s-b)*(s-c))**0.5

print('三角形面积为 %0.2f ' % area)
