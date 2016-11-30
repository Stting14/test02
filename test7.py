# -*- coding: UTF-8 -*-

# Filename : test7.py
# author by : STT

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False

print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.37'))
print(is_number('1e3'))

#测试unicode
# 阿拉伯语 5
print(is_number('٥'))  # False
# 泰语 2
print(is_number('๒'))  # False
# 中文数字
print(is_number('四')) # False
# 版权号
print(is_number('©'))  # False


str='12345'
print (str.isdigit())

str1='this is string example.....wow!!!'
print(str1.isdigit())


strr=u'string0123'
print(strr.isnumeric())

strrr=u'123456'
print(strrr.isnumeric())
