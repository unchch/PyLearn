# 给用户三次机会，猜想我们程序随机生成的一个数字A,每次用户猜想过后提示是否正确，以及用户输入额数字是大于A还是小于A
# 当机会用完提示用户已经输掉了游戏

import random

secert = random.randint(0,100)

times = 3 # 初始化用户的次数

while times:
    num = input("请输入数字：")
    if num.isdigit():
        tmp = int(num)
        if tmp == secert:
            print("你猜对了")
            break
        elif tmp < secert:
            print("你猜的太小了！！")
            times = times -1
        else:
            print("你的数字太大了！！")
            times = times - 1
    else:
        print("叫你输入数字！！")

print("你的3次机会用完了！")