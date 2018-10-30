import math
# print(math)
'''
# ceil() 向上取整操作
print(math.ceil(5.01))
print(math.ceil(5.9))

# floor() 向下取整操作
print(math.floor(5.01))
print(math.floor(5.9))

# 查看系统保留的关键字， 不可以用来当作变量命名
import keyword
print(keyword.kwlist)

for i in keyword.kwlist:
    print(i)
    
# round() 四舍五入，python 内置函数
print(round(5.01))
print(round(5.48))
print(round(5.5))
print(round(5.9))

# sqrt（） 开平方,返回浮点数
print(math.sqrt(4))

# pow（） 与幂运算相似，计算一个数的几次方,
# 有两个参数，第一个是底数，第二个是指数
# 返回一个浮点数
print(math.pow(4,3))
# 幂运算，返回的是整形，函数返回的是浮点型
print(4**3)

# fabs() 对一个数值获取绝对值，返回浮点数
print(math.fabs(5.1))
print(math.fabs(-3))
print(math.fabs(0))

# abs() 获取绝对值操作，不是数学模块中的，是python内置函数
# 返回值由本身而定
print(abs(-1))
print(abs(-2.5))
print(abs(0))
print(abs(4))

# fsum() 对整个序列求和, 返回浮点数
print(math.fsum([1,4,5,7]))

# sum() python内置求和函数,返回类型本身类型而定
print(sum([1,4.5,5,7]))

# math.modf() 将一个浮点数拆分为整数部分和小数部分组成元组
# 小数在前，整数部分在后
print(math.modf(4.5))
print(math.modf(0))
print(math.modf(4))
help(math.modf)

# copysign() 将第二个数的符号（正负号）传递个第一个数，返回第一个数的浮点数
print(math.copysign(2,-3))
print(math.copysign(-3,2))

# 打印自然对和和pi的值
print(math.e)
print(math.pi)

a = 5
print(5/10)
# 地板除，功能类似math.floor() 函数，向下取整
print(5//10)
print(a%10)

b = 25
print(b/10)
print(b//10)
print(b%10)

c = 125
print(c/10)
print(c//100)
print(c%100)
'''

# ascii码转数字
print(ord('A'))
print(ord('Z'))

print(ord('a'))
print(ord('z'))

# 数字转ascii码
print(chr(97))
print(chr(122))




