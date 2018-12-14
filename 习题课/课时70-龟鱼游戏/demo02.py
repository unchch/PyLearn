class CalNum(object):
    def get_num(self):
        x = input("请输入一个整数： ")
        new_x = -int(x)
        return new_x


n1 = CalNum()
print(n1.get_num())