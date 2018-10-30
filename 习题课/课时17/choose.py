import rand_math
import rand_zimu

print("请选择游戏：\n1.数字游戏\n2.字母游戏")
game = input("输入1或2: ")

if game == '1':
    # 实例化对象
    game_num = rand_math.GameNum()
    game_num.num_game(0,0)
elif game == '2':
    game_zimu = rand_zimu.GameZimu()
    game_zimu.a()
    game_zimu.j()
else:
    print('输入错误！请重新输入')
