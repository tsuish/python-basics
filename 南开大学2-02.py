"""
@File: 南开大学2-02.py
@Author: cuishuohao
@Date: 2026/3/10
"""
# https://www.icourse163.org/learn/NKU-1205696807?tid=1472095441#/learn/content?type=detail&id=1257325575&cid=1290717353

'''
数字数据类型分为：
    - 整型int
    - 浮点型float
    - 复数类型complex
'''

'''
整数可以用不同的进制来表示
    - 十进制：不加前缀
    - 八进制：加前缀0o
    - 十六进制：加前缀0x
Boolean类型是整型的子类型
    - True可转为1
    - False可转为0
'''
def func_1():
    a,b,c = 10,0o10,0x10
    # 输出对应的十进制结果：10 8 16
    print(a,b,c)

func_1()