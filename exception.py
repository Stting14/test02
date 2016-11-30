try:
    f=open('ddd.txt')
    print(f.read())
    f.close()
except OSError as err:
    print('文件出错了\n错误的原因是：'+ str(err))
