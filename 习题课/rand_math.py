import random
import math

# 输入函数
num = input("请输入一个三位数：")
# 检测输入是否是纯数字, 输入函数输入的是字符类型，不强制转换会报错
if num.isdigit() and 100 <= int(num) <= 999:
    # 判断输入的数，与系统随机数比较大小，符合条件则进行math操作
    num2 = random.randrange(100,999,1)
    print(num2)

    if int(num) >=  num2:
        print(math.sqrt(int(num)))
    else:
        print(math.pow(int(num),2))
else:
    print("请按规定输入： ")