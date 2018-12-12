# 子类调用父类普通方法
class Base(object):
    def __init__(self):
        print("Base init...")

    def run(self):
        print("Base running...")

class Leaf(Base):
    def __init__(self):
        Base.__init__(self)
        Base.run(self)
        print("Leaf running...")

a = Leaf()
print("=" * 30)

# 子类使用super方式调用父类方法
class Root(object):
    def __init__(self):
        print("I'm Root init...")

    def eat(self):
        print("I'm Root eating...")

class Normal(Root):
    def __init__(self):
        super().__init__()
        super().eat()

b = Normal()