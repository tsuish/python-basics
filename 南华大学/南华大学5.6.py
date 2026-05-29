# -*- coding: utf-8 -*-
# @Time : 2026/5/29 16:10
# @Author : Cui ShuoHao
# @File : 南华大学5.6.py

# https://article.xuexi.cn/articles/video/index.html?art_id=9480399107358912446&read_id=72c95f65-0d71-45ee-9ecb-10212c23d2ef&ref_read_id=6f09c3de-86ea-4826-8d4e-2c97b58f0061&reco_id=&mod_id=&cid=&source=&study_style_id=undefined
# 5.6 程序的异常处理——完美程序存在吗？

# 输入数字正常，输入非数字报错
def func1():
    num = eval(input("请输入一个整数："))
    print(num**2)

def func2():
    try:
        num = eval(input("请输入一个整数："))
        print(num**2)
    except NameError:
        print("请输入整数，而不是字符")
    except SyntaxError:
        print("请输入整数，而不是符号")
    except Exception as e:
        print(e)

def func3():
    try:
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        idx = eval(input("请输入一个整数："))
        print(str[idx])
    except NameError:
        print("请输入整数，而不是字符")
    except Exception as e:
        print(e)
    except:
        print("其他错误")

def func4():
    try:
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        idx = eval(input("请输入一个整数："))
        print(str[idx])
    except NameError:
        print("请输入整数，而不是字符")
    except Exception as e:
        print(e)
    else:
        print("没有发生异常")
    finally:
        print("程序执行完毕，不知道是否发生了异常")

# func1()
# func2()
# func3()
func4()