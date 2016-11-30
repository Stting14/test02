def factorial(n):
    result=n
    for i in range(1,n):
        result *=i

    return result
            
number=int(input('请输入一个数字：'))
result=factorial(number)
print('%d 的阶乘是: %d'% (number,result))



def factor(n):
    if n==1:
        return 1
    else:
        return factor(n-1)*n
number=int(input('请输入一个正整数：'))
result=factor(number)
print('%d 的阶乘是: %d'% (number,result))

 
def F(n):
    if n<1:
        print('输入有误！！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)

result=F(35)
if result!=-1:
    print('总共有%d只小兔崽子出生' % result)

def fab(n):
    
    
