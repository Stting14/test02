# -*- coding: UTF-8 -*-

# Filename : test25.py
# author by : STT

#获取昨天的日期

import datetime
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

print(getYesterday())
