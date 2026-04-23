"""
@File: 南华大学5.3.py
@Author: cuishuohao
@Date: 2026/4/23 21:45

https://article.xuexi.cn/articles/video/index.html?art_id=3807742763661652470&read_id=a6c98fca-7d8c-4478-bedd-a3bd4d14093b&ref_read_id=70b64cbf-e2e9-4e4e-b2ff-7e7e890c0c70&reco_id=&mod_id=&cid=&source=&study_style_id=undefined
5.3 for循环结构——国王与米粒的故事
"""

# for语句遍历字符串
def func_1():
    s = ""
    for i in "ABC":
        s = s+i*2
    print(s)

# 国王与米粒的故事，国际象棋格格里放米
def func_2():
    s = 0
    for i in range(1,65):
        s = s+pow(2,i-1)
    print("国王要给大臣的米粒数为：",s)

# for循环中的else
def func_3():
    for s in "BIT":
        print("循环进行中："+s)
    else:
        s = "循环正常结束"
    print(s)


# func_1()
# func_2()
func_3()