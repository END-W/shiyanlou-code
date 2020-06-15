#!/usr/bin/env python3
'''
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所以的赌注

Version 0.1
Author: END
'''
from random import randint

money = 1000
while money > 0:
    print('你的资产为：',money)
    needs_go_on = False#先设为假
    while True:#只要money不小于0就会执行这个input
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)#随机的点数
    print('玩家摇出了%d点'% first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:#就是needs_go_on==True执行这个代码
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜!')
            money -= debt
        elif current == first:
            print('玩家胜!')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束!')
