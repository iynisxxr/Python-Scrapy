# 任务4:字符串s="Lenovo" ,取出"v"字符
s = "lenovo"
print(s[4])

# 任务5:字符串s1="Lenovo" s2="python",将s1和s2组合成新的字符串
s1 = "lenovo"
s2 = "python"
print(s1 + s2)

# 任务6:字符串s1="Lenovo"   s2="python"，使用切片将s1的前三个字符和s2的后3个字符拼接为新字符串s3
s1 = "lenovo"
s2 = "python"
s3 = s1[:3] + s2[3:]
print(s3)

# 任务7:字符串s1="Lenovo" ,取出s1前三位赋值为s2，s2拼接字符串"_python_"和s1的后3位组成信息内容
s1 = "Lenovo"
s2 = s1[:3]
s3 = s2 + "_python_" + s1[3:]
print(s3)

# 任务8:如何将字符串"20" 和数值 10 进行相加，输出结果
s1 = "20"
s2 = 10
print(s1 + s2) # 报错：字符串型 和 整形 无法进行相加运算

# 任务9:定义列表类型变量my_group，保存本组一半成员名称，个人的放在第一位
my_group = ["颜xx","周xx","陈xx","梁xx"]
print(my_group)

# 任务10:向my_group追加信息成员"Tom"
my_group.append("Tom")

# 任务11:向my_group索引为1的位置插入新成员"Bill"
my_group.insert(1,"Bill")

# #任务12:删除索引为2的元素
del my_group[2]

# #任务13:删除my_group中的Bill
my_group.remove("Bill")

# 任务14:打印出 2、22.2 和“程序猿” 都是什么类型
s1 = 2
s2 = 22.2
s3 = "程序猿"
print(type(s1),type(s2),type(s3))

# #任务15:my_list =['张天爱',"杨幂",["赵丽颖","明明"],"杨紫", '迪丽热巴'],如何取出元素“明明”
my_list = ["张天爱","杨幂",["赵丽颖","明明"],"杨紫","迪丽热巴"]
print(my_list[2][1])

# #任务16:修改my_list中“杨紫”为"Rose"
my_list[3]="Rose"