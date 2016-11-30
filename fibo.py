#!/usr/bin/python3
# Filename: fibo.py

#def fib(n):    # 定义到 n 的斐波那契数列
#    a, b = 0, 1
#    while b < n:
#        print(b, end=' ')
#        a, b = b, a+b
#    print()
#
#def fib2(n): # 返回到 n 的斐波那契数列
#    result = []
#    a, b = 0, 1
#    while b < n:
 #       result.append(b)
 #       a, b = b, a+b
#    return result

#class MyClass:
#    '''一个简单的实例'''
#    i=12345
#    def f(self):
#        return 'Hello world!!!'
#实例化类
#x=MyClass()

#访问类的属性和方法
#print("MyClass 类的属性i为：",x.i)
#print("MyClass 类的方法 f 输出为：",x.f())


#class people:
    #定义基本属性
#    name=''
#    age=0
    #定义私有属性，私有属性在类外部无法直接进行访问
#    __weight=0
    #定义构造方法
#    def __init__(self,n,a,w):
#        self.name=n
#        self.age=a
#        self.__weight=w
#    def speak(self):
#        print("%s 说: 我 %d 岁。" %(self.name,self.age))


#class student(people):
 #   grade=''
 #   def __init__(self,n,a,w,g):
  #调用父类的构函
#        people.__init__(self,n,a,w)
#        self.grade=g
#    #覆盖父类的方法
#    def speak(self):
#        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade)")


#class speaker():
#              topic=''
#              name=''
#     def __init__(self,n,t):
#                  self.name=n
#                  self.topic=t
#     def speak(self):
#                  print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

    
        
#class sample(speaker,student):
#              a=''
#      def __init__(self,n,a,w,g,t):
#                  student.__init__(self,n,a,w,g)
#                  speaker.__init__(self,n,t)
#test=sample('Tim',25,80,4,'Python')
#test.speak()



#f=open('foo.txt',"wb")
#print("文件名为：",f.name)

#f.flush()
#
#fid=f.fileno()
#print("文件描述为：",fid)
#print("返回值为：",ret)
#f.close()

#try:
#    
#    f = open('foo.txt',"r")
 #   print("文件名为：",f.name)
#for index in range(5):
#        line=next(f)
#        print("第%d 行 - %s" % (index,line))
#except StopIteration:
 #       print("这是最后一行了")
#
#f.close()



#f=open('foo1.txt',"r+")
#print("文件名为：",f.name)

#line=f.readline()
#print("读取第一行：%s" % (line))

#line=f.readline(2)
#print("读取的字符串是： %s" % (line))

#f.seek(0,0)
#line=f.readline()
#print("读取的数据为：%s" % (line))

#pos=f.tell()
#print("当前位置为：%s" % (pos))

#f.truncate(10)
#line=f.readlines(3)
#print("读取行：%s" %(line))
#str=f.read()
#print ("读取数据: %s" % (str))

#str="6:www.runoob.com"
#f.seek(0,2)
#line=f.write(str)

#f.seek(0,0)
#try:
#    for index in range(6):
##        line=next(f)
#        print("文件行号%d -%s" % (index,line))
#except StopIteration:
#    print("到文件底部了！")


#f.close()


#f=open('foo1.txt',"w")
#print("文件名为：",f.name)
#seq=['菜鸟教程 1\n','菜鸟教程 2\n']
#f.writelines(seq)
#f.close()

#f=open('foo1.txt','r+')
#f.seek(0,0)
#try:
#    for index in range(8):
 #       line=next(f)
#        print("文件行号%d  %s"  %(index,line))
#except StopIteration:
#    pass
#f.close()



#import sys
#try:
#    f=open('foo01.txt')
#    s=f.readline()
#    i=int(s.strip())
#except OSError as err:
#    print("OS Error :{0}".format(err))
#except ValueError:
#    print("Could not conver data to an integer.")
#except:
#    print("Unexpected error:",sys.exc_info()[0])
#    raise

#import sys

#for arg in sys.argv[1:]:
#    try:
#        f=open(arg,'r')
#    except IOError:
#        print("cannot open",arg)
#    else:
#        print(arg,'has',len(f.readlines()),'lines')
#        f.close()


lower=int(input("输入区间最小值："))
upper=int(input("输入区间最da值："))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%2)==0:
                break
        else:
            print(num)
            
