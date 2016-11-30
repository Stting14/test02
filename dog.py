#age=int(input("请输入你家狗狗的年龄："))
#input("")
#if age<0:
  #  print("你是在逗我吗？")
#elif age==1:
   # print("相当于11岁的人")
#elif age==2:
 #   print("相当于22岁的人，")
#elif age>2:
#    human=11+(age-2)*11
#    print("相当于人的年龄：",human)

#print("点击Enter建退出")
#程序演示==操作符
#print(5==6)
#使用变量
#x=5
#y=6
#print(x==y)




#n=100

#sum=0
#counter=1
#while counter<=n:
#    sum=sum+counter
#    counter+=1
    
#print("1到%d的值为：%d"% (n,sum))

#print("1到%d的值为：%d"% (n,sum))
#n = 100


#ver=1
#while ver==1:
#    num=int(input("请输入一个数字:"))
#    print("你输入的数字是：",num)
#print("GoodBye")

#count=0
#while count<5:
#    print(count,"小于5")
 #   count+=1
#else:
#    print(count,"大于5")

#猜字迷游戏
#number=6
#guess=7
#print("##########猜字谜游戏开始###############")
#while guess!=number:
#    guess=int(input("请输入你猜的字谜："))

#    if guess==number:
 #       print("恭喜您，答对了！！！！")
 #   elif guess>number:
 #       print("很抱歉，猜da了……")
 #   elif guess<number:
 #       print("很抱歉，数字xiao了……")


#num=int(input("输入一个数字："))
#if num%2==0:
 #   if num%3==0:
#        print("您输入的数字可以整除2和3！！！")
#    else:
#        print("您输入的数字不可以整除2和3！！！！")
#else:
#    if num%3==0:
#        print("你输入的数字可以整除3但是不能整除2！！")
 #   else:
#        print("你输入的数字既不能整除3也不能整除2!!!!")


#count=5
#guess=4
#print("请输入一个数字")
#while guess!=count:
#    guess=int(input("你输入的值和count不等："))
#    if guess==count:
#        print("等于count!!!",guess)
#    elif guess>count:
#        print("大于count",guess)
#    elif guess<count:
#        print("小于count",guess)


#flag=1
#while (flag):print("欢迎来到菜鸟议程")
#print("Goodbye")


#languages = ["C", "C++", "Perl", "Python"]
#for x in languages:
#    print(x)

#sites=['baidu','google','runoob','taobao']
#for site in sites:
#    if site=='runoob111':
 #       print("菜鸟教程")
#        break
#    print("输入数据"+site)
#else:
#    print("没有输入数据")
#print("完成输入")


#for i in range(5):
#    print(i)

#for i in range(5,9):
 #   print(i)

#for i in range(0,10,3):
#    print(i)

#a=['baudu','google','taobao','tianmao','runoob']
#for i in range(len(a)):
#    print(i,a[i])
#    print(a[i])


#for letter in 'runoob':
#    if letter=='b':
#        break
#    print("当前字母为：",letter)


#letter={'baidu','google','runoob','robot'}
#'baidu' in letter


#question=['name','quest','favorite color']
#answer=['lancelot','the only grail','blue']
#for q,a in zip(question,answer):
#    print('what is your{0}?  it is {1}.'.format(q,a))

#for i in reversed(range(1,10,2)):
#    print (i)
#basket=['apple','orange','apple','pear','orange','banaer']
#for f in sorted(set(basket)):
#    print (f)



#import sys

#print("命令行参数如下：")
#for i in sys.argv:
#    print(i)

#print ('\n\npython 路径为：',sys.path,'\n')

#!/usr/bin/python3
# Filename: Hello.py

if __name__=='__main__':
    print('程序自身在运行')
else:
    print('我来自其他模块')


    
import Hello
Hello()


