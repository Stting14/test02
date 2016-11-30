# -*- coding: UTF-8 -*-

# Filename : test22.py
# author by : STT

#文件IO

#写文件

with open('foo.txt','wt') as out_file:
    out_file.write('该文本会写入到文件中\n看到我了吗\n看到啦')

#读文件
with open('foo.txt','rt') as in_file:
    text=in_file.read()

print(text)
