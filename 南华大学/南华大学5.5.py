# -*- coding: utf-8 -*-
# @Time : 2026/5/29 15:22
# @Author : Cui ShuoHao
# @File : 南华大学5.5.py

# https://article.xuexi.cn/articles/video/index.html?art_id=15211274900965494876&read_id=6f09c3de-86ea-4826-8d4e-2c97b58f0061&ref_read_id=e31121d4-ae72-4174-8193-e1837d35b4c1&reco_id=&mod_id=&cid=&source=&study_style_id=undefined
# 5.5 random库——绘制任意五角星

from random import random, randint, choice, randrange, shuffle, seed
import turtle

def func_1():
    print("random: ",random())

    print("randint: ",randint(0, 100))

    print("choice: ", choice([1,10,8,3,6,9]))

    # 生成一个0到100（不包含）的整数，且是4的倍数
    print("randrange: ", randrange(0,100,4))


    ls = [0,1,2,3,4,5,6,7,8,9]
    shuffle(ls)
    print("shuffle: ", ls)

    print("-"*20+"seed---start"+"-"*20)
    seed(125)
    print("{},{},{}".format(randint(1,10), randint(1,10),randint(1,10),))
    print("{},{},{}".format(randint(1,10), randint(1,10),randint(1,10),))
    seed(125)
    print("{},{},{}".format(randint(1,10), randint(1,10),randint(1,10),))
    print("-"*20+"seed---end"+"-"*20)

def func_2():
    for i in range(5):
        turtle.fd(100)
        turtle.rt(144)

def func_3():
    d = randint(50, 200)                        # 任意边长
    r = randrange(1,15,3)             # 任意粗细
    turtle.pensize(r)
    turtle.pencolor(random(),random(),random())      # 任意颜色
    for i in range(5):
        turtle.fd(d)
        turtle.rt(144)

# func_1()
# func_2()
func_3()