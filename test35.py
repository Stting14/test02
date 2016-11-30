#-*-:coding:UTF-8 -*-
# Filename : test35.py
# author by : STT
#!/usr/bin/python3

import json
#python字典类型转换为JSON 对象

import math
for i in range(0,10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if (x*x==i+100) or (y*y==i+268):
        print(i)
