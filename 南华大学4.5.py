#   https://article.xuexi.cn/articles/video/index.html?art_id=4750214679917237617
#   4.5 字符串格式化——format 方法

# 指定位置的两种方式
def func_1():
    name = '张三'
    content = '你好'
    print("{}，我想跟你说：{}".format(name,content))
    print(f"{name}，我想跟你说：{content}")

    # 方式一：不指定位置，按默认顺序
    print("{} {}".format("hello","world"))
    # 设置指定位置
    print("{0} {1} {0}".format("hello","world"))

    # 方式二：用参数指定
    print("网站：{s}，网址：{u}".format(s="百度",u="www.baidu.com"))


# 填充；对齐方式
def func_2():
    # "abc"宽度>1：按"abc"实际显示
    print("{0:1}".format("abc"))
    # "abc"宽度<10："abc"后面部分补空格
    #       {0:10}等同于{0:<10}，左对齐


    print("{0:10}".format("abc"))
    # {0:>10}，右对齐，左补7个空格（7=10-3）
    print("{0:>10}".format("abc"))
    # {:^10}，居中对齐，左3个空格，右4个空格
    print("{:^10}".format("abc"))
    # {:-^10}，居中对齐，左3个-，右4个-
    #   -可以换成=、+等字符
    print("{:-^10}".format("abc"))

    # {0:s}等价于{0:}，即按实际显示
    #   s表示类型是 字符串
    print("{0:s}".format("abc"))

    # 长度占10列，右对齐，左边用*补齐，小数点保留两位
    #   f表示类型是 浮点数
    #   .2控制精度
    print("{:*>10.2f}".format(3.14159))

    # 这里{0:b},{1:c}的0和1，用来指定位置，即对应位置0的10和位置1的65
    # b和c表示的是类型
    #   b表示类型是 二进制整数，{0:b}以二进制输出10，为”1010“
    #   c表示的是chr函数操作 返回Unicode编码65对应的字符，即"A"
    #       ASCII表：https://www.runoob.com/w3cnote/ascii.html
    print("{0:b},{1:c}".format(10,65))
    print(chr(65))

# 课后练习
def func_3():
    a = "Python"
    b = "A Superlanguage"
    print("{:->10}:{:-<19}".format(a,b))

# func_1()
# func_2()
func_3()