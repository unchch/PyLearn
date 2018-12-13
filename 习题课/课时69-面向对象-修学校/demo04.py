class People(object):
    address = "深圳"
    list1 = []

    def __init__(self, obj):
        self.name = "zhangsan"
        self.age = "20"
        self.list1.append(obj.num)



p  = People(2)

print(p.name)
print(p.age)


p.name = "lisi"
p.age = "30"

print(p.name)
print(p.age)
