import random
'''
# random() 获取0-1之间的随机小数，包含0不包含1
for i in range(10):
    # print(random.random())

    # 随机指定开始和结束之间的整数值
    # print(random.randint(1,9))

    # random.randrange() 获取指定开始和结束之间的整数值，可以指定间隔
    print(random.randrange(1,9,3))

# choice() 随机获取列表中的值
print(random.choice([1,2,56,980,87987]))

# shuffle() 随机打乱序列,返回值是空
print(random.shuffle([1,2,56,980,87987]))

list1 = [1,2,56,980,87987]
print(list1)

random.shuffle(list1)
print(list1)
'''

# uniform() 随机获取指定范围内的值（包括小数）
for i in range(10):
    print(random.uniform(1,9))

