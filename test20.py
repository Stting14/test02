# -*- coding: UTF-8 -*-

# Filename : test20.py
# author by : STT

#生成日历

import calendar

#输入指定年月
yy=int(input('请输入年份：'))
mm=int(input('请输入月份：'))

print(calendar.month(yy,mm))
