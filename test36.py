print('**************我爱鱼C工作室**************')
import random
i=random.randint(1,10)
guess=int(input('请输入一个数字：'))
while guess!=i:
    guess=int(input('请重新输入：'))
    if guess==i:
        print('卧槽，你是小甲鱼心凉的蛔虫吗？')
        print('哼，猜中了也没有奖励')
    else:
        if guess>i:
            print('哥，大了大了！！！！')
        else:
            print('嘿，小了，小了')
print('游戏结束，不玩了！！！')






