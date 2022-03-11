day5

一、复习

1.字典

定义：变量名 = {"key1":"value1","key2":"value2"}

添加：变量名["key"] = ["value"]

删除：del 变量名["key"]

获取：变量名["key"]

2.元组

定义：变量名 = （元素1，元素2，元素3）

3.转义字符

符号：

使用：str = 'It's a cat'

    my_str = "12345678\rmy"
    print(my_str)
    输出结果：my345678

4.格式化字符串

（1）%

符号：%s（字符串），%d（整数），%f（浮点数）

使用：变量名 = "我是%s，今年%d岁"%（"小明"，12）

（2）.format

使用：变量名 = "我是{}，今年{}岁".format（"小明"，12）

（3）f-string

使用：

    a = "小米"
    b = 12
    变量名 = f"我是{a}，今年{b}岁"

二、字符串

1.join

作用：将序列中的元素以指定的字符连接生成一个新的字符串

    my_list = ["小米","vivo","oppo","华为"]
    my_str = "_".join(my_list)
    print(my_str)
    # 输出结果：小米_vivo_oppo_华为

2.split

作用：通过指定分隔符对字符串进行切片

    my_str = "小米_vivo_oppo_华为"
    my_list2 = my_str.split("_")
    print(my_list2)
    # 输出结果：['小米', 'vivo', 'oppo', '华为']

3.strip

作用：移除字符串头尾指定的字符

    my_name = " 夏利\n"
    print(my_name)
    # 输出结果： 夏利
    （有换行）
    print(my_name.strip())
    # 输出结果：夏利

4.isdigit

作用：检测字符串是否只由数字组成

    a = "10"
    b = 20
    c = "牛啊"
    print(a.isdigit())
    # 输出结果：True
    print(b.isdigit())
    # 输出结果：报错,isdigit不支持int类型
    print(c.isdigit())
    # 输出结果：False

三、函数

定义：

    def 函数名(参数):
    代码内容

调用：函数名（参数）

