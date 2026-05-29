# -*- coding: utf-8 -*-
# @Time : 2026/5/29 9:52
# @Author : Cui ShuoHao
# @File : 南华大学5.4.py

# https://article.xuexi.cn/articles/video/index.html?art_id=852397308158177033&read_id=e31121d4-ae72-4174-8193-e1837d35b4c1&ref_read_id=a6c98fca-7d8c-4478-bedd-a3bd4d14093b&reco_id=&mod_id=&cid=&source=&study_style_id=undefined
# 5.4 break和continue语句——用户登录

def func1():
    for s in "PYTHON":
        if s=="T":
            break
        print(s,end="")

def func2():
    s=0
    while s<6:
        s=s+1
        if s==3:
            break
        print(s,end="")

def func3():
    for s in "PYTHON":
        if s=="T":
            continue
        print(s,end="")

def func4():
    s=0
    while s<6:
        s=s+1
        if s==3:
            continue
        print(s,end="")

# continue对else没有影响
def func5():
    for s in "PYTHON":
        if s=="T":
            continue
        print(s,end="")
    else:
        print("正常退出")

# break对else有影响
def func6():
    for s in "PYTHON":
        if s=="T":
            break
        print(s,end="")
    else:
        print("正常退出")

# 嵌套时，break语句只能跳出它所在的那层循环，不能越级跳
def func7():
    for s in "BIT":
        for i in range(3):
            print(s,end="")
            if s=="I":
                break

# 案例：用户登录
def func8():
    for i in range(3):
        username = input("用户名：")
        password = input("密码：")
        if username=='admin' and password=='123456':
            print("登录成功")
            break
        else:
            print("账号或密码不正确")

# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()