# https://www.icourse163.org/learn/NKU-1205696807?tid=1472095441#/learn/content?type=detail&id=1257325569&sm=1
# 1-04输入、输出及IDLE环境介绍

# 接收到的是str格式的字符串
def func_1():
    name = input("请输入你的姓名：")
    print(name)


def func_2():
    # eval函数计算字符串所对应的数学表达式的值，返回表达式的计算结果
    #   返回的类型是int
    #   如果是无效表达式，会报错
    r = eval(input("请输入一个有效的表达式："))
    print(r)
    print(type(r))




func_2()