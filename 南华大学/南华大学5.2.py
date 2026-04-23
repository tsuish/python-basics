"""
@File: 南华大学5.2.py
@Author: cuishuohao
@Date: 2026/4/23 13:17

https://article.xuexi.cn/articles/video/index.html?art_id=16580888374631742746&read_id=70b64cbf-e2e9-4e4e-b2ff-7e7e890c0c70&ref_read_id=5f795b70-6c97-4614-85db-9e354f9f02fc&reco_id=&mod_id=&cid=&source=&study_style_id=undefined
5.2 程序的选择结构——身材评判
"""

# 单分支选择结构
def func_1():
    sg = eval(input("请输入身高（cm）:"))
    xb =input("请输入性别（男｜女）：")
    if xb == "女":
        bztz = (sg-105)*0.92
    if xb == "男":
        bztz = (sg-105)*0.9

    print("标准体重为：{:.2f} kg".format(bztz))

# 双分支选择结构
def func_2():
    sg = eval(input("请输入身高（cm）:"))
    xb = input("请输入性别（男｜女）：")
    if xb == "女":
        bztz = (sg - 105) * 0.92
    else:
        bztz = (sg - 105) * 0.9

    print("标准体重为：{:.2f} kg，即{:.2f}斤".format(bztz, bztz*2))

# 选择结构的嵌套
def func_3():
    sg,tz = eval(input("请输入身高（厘米）,体重（公斤）："))
    xb = input("请输入性别（男｜女）：")
    if xb == '女':
        bztz = (sg - 105) * 0.92
        if tz>bztz*1.1:
            print("偏胖")
        else:
            print("不胖")
    else:
        bztz = (sg - 100) * 0.9
        if tz > bztz * 1.1:
            print("偏胖")
        else:
            print("不胖")

# 多分支选择结构： if-elif-else语句
def func_4():
    sg, tz = eval(input("请输入身高（厘米）,体重（公斤）："))
    xb = input("请输入性别（男｜女）：")
    if xb=='男':
        bztz = (sg - 100) * 0.9
    else:
        bztz = (sg - 105) * 0.92
    r = (tz - bztz)/bztz
    if r>=0.2: print("太胖")
    elif r>=0.1: print("偏胖")
    elif r>=-0.1: print("标准")
    elif r>=-0.2: print("偏瘦")
    else: print("太瘦")

# func_1()
# func_2()
# func_3()
func_4()