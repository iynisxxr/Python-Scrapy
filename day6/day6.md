day6

一、复习函数

1.实参和行参

2.位置参数和关键词参数

二、函数

1.任意参数

    位置参数：*args    关键字参数：**kwargs

2.return函数

作用：终止def函数并返回指定值

    返回单个值：return 值
    返回多个值：return 值1，值2
    注：返回多个值是以元组形式返回

三、函数作用域

定义：在函数内部的变量拥有一个局部作用域，在函数外的拥有全局作用域

局部变量：只能在其被声明的函数内部访问

全局变量：可以在整个程序范围内访问

调用函数：在函数内声明的变量名称都将被加入到作用域中

五、可变类型

定义：修改其数值，内存地址不变

种类：列表、字典、集合

六、内置函数

1.类型转换

2.数学类

3.其他

七、冒泡排序

    两两对比，大的换位，小的不变
    lst = [1,2,5,75,123,13,73,54,76,21,25]
    for i in range(len(lst)):
    for j in range(len(lst)-1-i):
    if lst[j] > lst[j+1]:
    lst[j],lst[j+1] = lst[j+1],lst[j]
    print(lst)
