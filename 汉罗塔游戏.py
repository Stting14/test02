def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1的盘子移动到y上
        print(x,'-->',z)#将最底下的最后一个盘子移动到从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1歌盘子一到z上

n=int(input('请输入汉罗塔的层数：'))
hanoi(n,'x','y','z')
    
