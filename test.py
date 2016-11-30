# _*_ coding: UTF-8 _*_

#FileName : test.py

# author by: STT

# 用户输入数字
#num1=input('请输入第一个数字：')
#num2=input('请输入第二个数字：')

#求和
#sum=float(num1)+float(num2)

#显示计算结果

#print('数字{0}和{1}相加的结果为：{2}'.format(num1,num2,sum))


#直接打印
#print('两数之和为 %.lf' %(float(input('请输入第一个数字：'))
#                     +float(input('请输入第二个数字：'))))

#num=float(input('请输入第一个数字：'))
#num_sqrt=num**0.5
#print('%s 的平方根为%s'%(num,num_sqrt))


#计算实数和复数的平方根
#导入复数数学模块

import cmath

num=int(raw_input("请输入一个数字: "))
num_sqrt=cmath.aqrt(num)
print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))
