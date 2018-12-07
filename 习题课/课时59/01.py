# name = input("请输入你的姓名： ")
# print("你好，" + name)

temp = input("请输入一个零到一百的整数：")
if temp.isdigit():
    temp = int(temp)
    if 1 <= temp <= 100:
        print("你好看")
    else:
        print("你丑八怪，天黑别把灯打开")
else:
    print("丑八怪，天黑别把灯打开")