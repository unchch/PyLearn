import random
import tkinter


class RandomBall(object):
    '''
    定义运动球的类
    canvas 画布，所有内容应该在画布上呈现，此处通过变量来呈现
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):

        self.canvas = canvas
        # 球出现的初始位置要随机，此位置是球的圆心
        # xpos 表示位置的x座标
        self.xpos = random.randint(30, int(scrnwidth) - 20)
        # ypos 表示位置的y座标
        self.ypos = random.randint(20, int(scrnheight) - 30)

        # 定义球运动的速度
        # 模拟运动：不断的擦掉原来的画，然后在新的位置再重新绘制
        # 此处 xvelocity 模拟x方向的运动
        self.xvelocity = random.randint(4, 20)
        # 同理  yvelocity 模拟y方向的运动
        self.yvelocity = random.randint(4, 20)

        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        # 定义屏幕的高度
        self.scrnheight = scrnheight

        # 球的大小随机
        # 此处球的大小用半径来定义
        self.radius = random.randint(20, 120)

        # 球的颜色随机
        # RGB表示法，三个数字 0-255，红绿蓝；某些系统可以用单词，例如 red green blue
        # 此处用lambda 表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球
        '''
        # tkinter没有画圆形函数，只有画椭圆函数
        # 画椭圆需要定义两个座标
        # 在一个长方形内画椭圆，我们只需要定义长方形的两个对角
        # 求两个坐标的方法，已知圆心座标，则圆心座标减去半径，能得出左上角，加上半径，能得出右下角
        x1 = self.xpos - self.radius
        # 继续求 y1 x2 y2
        y1 = self.ypos + self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos - self.radius

        # 在有两个对角坐标的前提下，可以画圆
        # fill 表示填充颜色
        # outline 是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的时候，需要控制球的移动方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        # 同理计算yops
        self.ypos += self.yvelocity

        # 以下判断是否会撞墙，注意球的半径
        # 撞到了右边墙
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity = -self.xvelocity  # 或者self.xvelocity *= -1
        # 撞到左边墙
        if self.xpos <= self.radius:
            self.xvelocity = -self.xvelocity
        # 撞到上边墙
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity
        # 撞到下边墙
        if self.ypos <= self.radius:
            self.yvelocity = -self.yvelocity

            # 在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    '''
    定义屏保的类
    可以被启动
    '''

    def __init__(self):
        # 如何装随机产生的球
        self.balls = list()
        # 每次启动球的数量是随机的
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都要取消屏保
        self.root.bind('<Motion>', self.myquit)
        # 同理 任何键盘按键都要退出
        self.root.bind('<Key>', self.myquit)

        # 得到屏幕的大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after 是200毫秒后启动一个函数，需要启动的函数是第二个参数指定的函数
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self, e):
        # 此处利用了时间处理机制，实际并不关心时间的类型
        # 销毁函数，与init相反
        self.root.destroy()


if __name__ == "__main__":
    # 启动屏保
    ScreenSaver()