# -*- coding: UTF-8 -*-

# Filename : test21.py
# author by : STT

def recur_fibo(n):
    """递归函数
   输出斐波那契数列"""
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

#获取用户输入

num=int(input('您要输入几项？？'))

#检查输入的正确性
if num<=0:
    print('输入整数')
else:
    print('斐波那契数列：')
    for i in range(num):
        print(recur_fibo(i))
