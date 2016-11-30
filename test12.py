# -*- coding: UTF-8 -*-

# Filename : test12.py
# author by : STT

#九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i,j,i*j),end='')
       
    print()
