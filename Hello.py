#import fibo
#
##fibo.fib(100)
#fibo.fib2(1000)
#fibo.__name__

#str=input("请输入：");
#print("您输入的内容是：",str)

#f=open("foo.txt",'w')
#f.write("python 是一个非常好的语言。\n是的，非常更好！！！\n")
#f.close()

#f=open("foo.txt",'r')

#str=f.readline()
#
#print(str)
#f.close()



#f=open("foo.txt","r")
#str=f.readlines()
#print(str)
#f.close()

#f=open("foo.txt","r")
#for line in f:
#    print(line,end='')
#f.close()

#f=open("foo.txt","w")
#num=f.write("Python 是一个非常好的语言。\n是的，是非常好的语言！！！\n")
#print(num)
#f.close()


#f=open("foo.txt","w")
#value=('www.runoob.com',14)
#s=str(value)
#f.write(s)
#f.close()

#fo=open('foo.txt','wb')
#print('文件名为：',fo.name)

#for index in range(5):
 #   line=next(fo)
#    print("第%d行-%s" % (index,line))

#fid=fo.fileno()
#print("文件描述为：",fid)

#ret=fo.isatty()
#print("返回值为：",ret)

#fo.flush()

#fo.close()


#fo=open('foo.txt','r')
#print('文件名为：',fo.name)
#try:
#    for index in range(3):
#        line=next(fo)
#        print("第%d行-%s" % (index,line))
#except StopIteration:
 #   print( 'here is end '),index

#fo.close()


#fo =open("foo.txt",'r+')
#print("文件名为：",fo.name)
#
#line=fo.readline()
#print("读取第一行的数据 %s" %(line))

#str="6:wwww.runoob.com"


#fo.seek(0,2)
#line=fo.write(str)

#fo.seek(0,0)
#for index in range(6):
#    line=next(fo)
 #   print("文件行号 %d-%s" % (index,line))


#print("读取的字符串是：%s" % (line))

#pos=fo.tell()
#print("当前位置为：%d" % (pos))
#fo.close()

#fo=open("foo.txt","w")
#print("文件名为：",fo.name)
#seq=["菜鸟教程 1\n","菜鸟教程 2"]
#fo.writelines(seq)
#fo.clos



#import sys,os
#ret=os.access('foo.txt',os.F_OK)
#print("F_OK-返回值 %s" % ret)

#ret=os.access('foo.txt',os.R_OK)
#print("R_OK-返回值 %s" % ret)

#ret=os.access('foo.txt',os.W_OK)
#print('W_OK-返回值 %s' % ret)
#
#ret=os.access('foo.txt',os.X_OK)
#print('X_OK-返回值 %s' % ret)


#while True:
#     try:
#        x=int(input("Please Enter a number:"))
#         break
#     except ValueError:
#        print("Oops!That was no valid number,Try again!")


#import sys
#try:
#    f=open('foo.txt')
#    s=f.readline()
#    i=int(s.strip())
#except OSError as err:
#    print("OS error:{0}".format(err))
#except:
#    print("Unexceptd error:",sys.exc_info()[0])
#    raise

import sys
for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print('cannot open',arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()
