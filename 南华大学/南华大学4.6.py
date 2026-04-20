"""
@File: 南华大学4.6.py
@Author: cuishuohao
@Date: 2026/4/20

https://article.xuexi.cn/articles/video/index.html?art_id=9258265869200543912&read_id=1a62a21e-0c8b-423f-88e3-d28bc31ed6f7&ref_read_id=3b41236f-c847-415c-8998-d24282ee02e3&reco_id=&mod_id=&cid=&source=&study_style_id=undefined
4.6 字符串格式化——文本进度条
"""


def func_1():
    c = 0
    for i in range(11):
        a='**'*i
        b='..'*(10-i)
        print("{:>3}%[{}->{}]".format(c,a,b))
        c = c + 10

def func_2():
    print("--------执行开始-----------")
    scale = 20
    for i in range(scale + 1):
        a='**'*i
        b='..'*(scale-i)
        c = (i / scale) * 100
        print("{:>3.0f}%[{}->{}]".format(c,a,b))
    print("--------执行结束-----------")

# 单行动态刷新
#   后显示的字符覆盖之前的字符
# python run，或终端命令：python 南华大学/南华大学4.6.py
def func_3():
    import time
    print("--------执行开始-----------")
    scale = 20
    for i in range(scale + 1):
        a='**'*i
        b='..'*(scale-i)
        c = (i / scale) * 100
        # \r：光标退回到行开头的位置
        # end=''：输出的时候不能换行
        print("\r{:>3.0f}%[{}->{}]".format(c,a,b),end='')
        time.sleep(0.2)
    print("\n--------执行结束-----------")


# 带刷新的文本进度条
def func_4():
    import time
    scale = 20
    print("执行开始".center(scale,'-'))
    start = time.perf_counter()
    for i in range(scale + 1):
        a='**'*i
        b='..'*(scale-i)
        c = (i / scale) * 100
        t = time.perf_counter() - start
        # \r：光标退回到行开头的位置
        # end=''：输出的时候不能换行
        print("\r{:>3.0f}%[{}->{}]{:.2f}s".format(c,a,b,t),end='')
        time.sleep(0.4)
    print()
    print("执行结束".center(scale, '-'))

# func_1()
# func_2()
# func_3()
func_4()