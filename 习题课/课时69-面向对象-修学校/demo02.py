class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")

    def shouting(self):
        print("Dog can shout loudly...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

class Tortoise(Animal):
    def run(self):
        print("Tortoise is runing slowly...")


class Timer(object):
    def run(self):
        print("starting ...")

def run_twice(animal):
    animal.run()
    animal.run()


# 多态,只要传入twice的参数是Animal类型即可,会自动调用run 方法,若子类没有run方法,则会调用父类的run方法
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

# 鸭子模型,传入的参数甚至只要有run方法,甚至不需要是Animal类型,即可调用函数
run_twice(Timer())