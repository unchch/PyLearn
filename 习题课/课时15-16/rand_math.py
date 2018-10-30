import random
import math

'''
输入一个三位数，与程序随机数比较大小
1、如果大于，则分别输出这个三位数的个位、十位和百位
2、如果等于，则提示中奖，计100分
3、如果小于，则将120个字符输入到文本文件中（规则是每条字符串的长度为12，单独占一行，前4个是字母，后8个是数字）
'''

def line():
    # 定义一个空字符串，用于拼接字符
    str_num = ''
    # 随机前4个字母（用ascii码对应的值来循环，再转换为字母）
    for i in range(4):
        # 随机消息字母的arcii码值
        num = random.randrange(97,123)
        # 将ascii码值转换为对应的字母
        str_s = chr(num)
        # 依次拼接得到随机额字母
        str_num = str_num + str_s

    # 循环后8个随机数字
    for i in range(8):
        num = random.randrange(0,10)
        str_num = str_num + str(num)

    return str_num

def num_game(total, source):
    while 1:
        # 输入函数
        num = input("请输入一个三位数，输入-1结束：")
        if num == "-1":
            break
        # 程序随机数
        random_num = random.randrange(100,1000)
        # 检测输入是否是纯数字和3位数, 输入函数输入的是字符类型，不强制转换会报错
        if num.isdigit() and 100 <= int(num) <= 999:
            # 计算有效输入的次数
            total += 1
            print("有效输入%d次"%total)
            num = int(num)
            random_num = int(random_num)
            # 判断输入与随机数的大小
            if num > random_num:
                # 求百位数字的方法 - 地板除100取整 或 用math.floor()
                bai = num // 100
                # 求十位，先除100取模（取余），再地板除10
                shi = num % 100 // 10
                # 求个位数，直接取10的模（取10的余）
                ge = num%10
                print('你输入的数比随机数大，随机数是', random_num)
                print("这个三位数的个位是{}，十位是{}，百位是{}".format(ge, shi, bai))
            if num == random_num:
                # 所得的分数
                source = source + 100 # source += 100
                print("你中奖了，目前分数为", source)
                print("你中奖的概率是多少",source/total)
            if num < random_num:
                # 由于120个字符，每行12个，可知存入10行就可以
                print('你输入的数比随机数小，随机数是',random_num)
                for i in range(10):
                    str_line = line()
                    # print(str_line)
                    # 执行文件存入操作
                    with open('str_num.txt','a') as f:
                        f.write(str_line + '\n')
        else:
            print("请按规定输入三位数： ")

if __name__ == '__main__': # 程序入口（调试代码）
    print(__name__) # 在当前模块中，__name__ = __main__,当第三方导入时，__name__ = 文件名
    # 定义一个变量，用于存储初始分数
    source = 0
    # 定义一个变量，用于累计输入了多少次
    total = 0

    num_game(total, source)
