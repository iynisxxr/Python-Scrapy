day7

一、函数名的运用

定于：函数名本质上也是一个变量，可以重新赋值，但是函数是一个特殊的变量，是一个可以搭配括号执行函数的变量

    def func():
    print("函数func")
    func() # 输出：函数func
    func = 10
    func() # 此时会报错,因为此时func引向了10,而不是函数的内存地址

二、函数套娃(函数名可以当作参数被调用，也可以当作函数的返回值)

    套娃一：
    def func1():
    print("func1")
    def func2(func):
    print("func2")
    func()
    print("func2")
    func2(func1)
    # 输出结果：
    # func2
    # func1
    # func2
    
    套娃二：
    def func1():
    print("func1")
    def func2(func): # 将func1 当作参数传进来作为 func
    print("func2")
    return func
    fn = func2(func1)
    fn() # 此时fn() 相当于 func() 相当于 func1()
    # 输出结果：
    # func2
    # func1

三、闭包与函数引用

闭包：在函数内定义一个新的函数

引用：函数也是一个变量，只是能通过搭配括号进行执行函数

    def func1():
    def func2():
    print("func2")
    return func2
    func2() # 报错，内嵌函数无法调用在外部中被调用
    
    # 函数引用一：
    def func1():
    print("func1")
    def func2():
    print("func2")
    a = func2
    b = func2
    print(a())
    print(b())
    print(func2())
    func1()
    # 输出结果：
    # func1
    # func2
    # func2
    # func2
    
    # 函数引用二：
    def func1(a,b):
    c = 10
    def func2(x):
    return a * b + x
    return func2
    func = func1(4,5)
    print(func(5))
    # 输出结果：55

四、装饰器

定义：在不改变原有函数的基础上添加新功能

    # 方式一：
    def func1(func):
    def func2():
    print("func2开始")
    func()
    print("func2结束")
    return func2
    def func3():
    print("func3")
    func3 = func1(func3)
    func3()
    
    # 方式二：
    def func1(func):
    def func2():
    print("func2开始")
    func()
    print("func2结束")
    return func2
    @func1    # 相当于func3 = func1(func3)
    def func3():
    print("func3")
    func3()

五、迭代器与生成器

迭代器：从第一个元素开始访问，直到所有的元素被访问完

生成器：使用了 yield 的函数被称为生成器（在调用生成器运行过程中，每次遇到 yield 函数时会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行）

    # 迭代器：
    lst1 = [1,2,3]
    lst = lst1.__iter__()
    print(lst.__next__())
    print(lst.__next__())
    print(lst.__next__())
    # print(lst.__next__())
    # 元素不够拿，程序报错,得重新生成迭代器才能遍历元素
    lst = lst1.__iter__()
    print(lst.__next__())
    # 输出结果：
    # 1
    # 2
    # 3
    # 1


​    
​    # 生成器：
​    def func():
​    for a in range(1,10):
​    yield "a:"+str(a)
​    b = func()
​    print(b.__next__())
​    print(b.__next__())
​    print(b.__next__())
​    # 输出结果：
​    # a:1
​    # a:2
​    # a:3

六、推导式

    # 列表推导式：
    lst = [i for i in range(1,10)]
    print(lst)
    # 输出结果：[1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    lst = [i for i in range(1,10) if i % 2 == 0]
    print(lst)
    # 输出结果：[2,4,6,8]
    
    # 生成器推导式：
    a = ("第%s次" % i for i in range(3))
    for i in a:
    print(i)
    # 输出结果：
    # 第0次
    # 第1次
    # 第2次
    
    # 字典推导式
    lst1 = ["孙悟空","猪八戒","唐僧"]
    lst2 = ["猴","猪","人"]
    dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
    print(dic)
    # 输出结果：{'孙悟空': '猴', '猪八戒': '猪', '唐僧': '人'}



















