# -*- coding: UTF-8 -*-

# Filename : test27.py
# author by : STT


#正则表达式

import re
print(re.match('www', 'www.runoob.com').span())  
print(re.match('com', 'www.runoob.com'))

print(re.search('www','www.runoob.com').span())
print(re.search('com','www.runoob.com').span())
