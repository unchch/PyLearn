# 收集参数的解包问题

def stu(*args):
    print("hello")

    # 此处的循环仅调试用，为了验证 list 内的元素是否被解包并循环打印
    n = 0
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)


l = ["liuying", 20, 230]
stu(l)

print("=" * 20)

# 此时 args 的表现形式是 tuple 类型，里层是一个 list，即 arg = (['liuying', 20, 230],) 整体作为一个参数
# 很显然和我们最初的的想法相违背
# 此时的调用，我们需要用解包符号，即调用前面加一个 * 符号
stu(*l)
print("=" * 20)