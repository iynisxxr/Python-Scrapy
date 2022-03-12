# 任务4
"""
用户输入的整数,判断用户输入的是奇数还是偶数：
要求：
1.纸上画出流程图拍照(如果使用软件能画流程更好)
2.按照流程图书写代码，注意些注释
"""
n = int(input("输入一个数："))
if n % 2 == 0:
    print(f"你输入的整数{n},它是偶数")
else:
    print(f"你输入的整数{n},它是奇数")

# 任务5
"""
判断输入的年龄大于或等于50，
输出"你不适合做编程"，否则输出"程序猿欢迎您"
"""
age = input("请输入您的年龄：")
if age >= "50":
    print("你不适合做编程")
else:
    print("程序猿欢迎你")

# 任务6:实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
while True:
    user = input("请输入你的账号：")
    pwd = input("请输入你的密码：")
    if user == "seven" and pwd == "123":
        print("登录成功")
        break
    else:
        print("登录失败")

# 任务7
"""
input函数接收用户的输入，用户输入3个正整数，中间用空格分开，请写程序判断这3个整数能否构成三角形：
分析：1.字符串的split方法分割输入内容
要求： 
1. 纸上画流程图拍照(如果使用软件能画流程更好)
2.按照流程图书写代码，注意些注释
"""
list = input("输入三个整数(空格分割)：")
list_value = list.split(" ")
a,b,c = int(list_value[0]),int(list_value[1]),int(list_value[2])
if a + b > c and a + c > b and c + b > a:
    print("是三角形")
else:
    print("不是三角形")

# 任务8
"""
使用input函数接收用户输入，用户会输入两个整数，中间用空格分割，
程序输出两个数中最大的一个：
需求： 
1. 纸上画流程图拍照(如果使用软件能画流程更好)             
2.按照流程图书写代码，注意些注释分析
提示：
1.字符串的split方法分割输入内容
"""
# list = input("输入两个数（两个分隔）")
# list_value = list.split(" ")
# print(max(list_value))
list = input("输入两个数（两个分隔）")
list_value = list.split(" ")
max = list_value[0]
if list_value[1] > max:
    max = list_value[1]
print(max)

# 任务9
"""
使用input函数接收用户输入，用户会输入三个整数，中间用空格分割，
程序输出两个数中最大的一个：
需求： 
1. 纸上画流程图拍照(如果使用软件能画流程更好)            
2.按照流程图书写代码，注意些注释分析
提示：
1.字符串的split方法分割输入内容
"""
list = input("输入三个数（两个分隔）")
list_value = list.split(" ")
max = list_value[0]
if list_value[1] > max:
    max = list_value[1]
elif list_value[2] > max:
    max = list_value[2]
print(max)

# 任务10:lst = [4, 6, 1, 7, 2, 9, 3] 需求：找出列表最大值
list = [4, 6, 1, 7, 2, 9, 3]
print(max(list))

# 任务11:lst = [4, 6, 1, 7, 2, 9, 3] 需求：找出列表最二大值
list = [4, 6, 1, 7, 2, 9, 3]
list.remove(max(list))
print(max(list))

# 任务12
"""
成绩有ABCDE5个等级，与分数的对应关系如下:
A    90-100
B    80-89
C    60-79
D    40-59
E    0-39根据输入的成绩输出不同的等级
需求： 
1. 纸上画流程图拍照(如果使用软件能画流程更好)             
2.按照流程图书写代码，注意些注释
"""
score = int(input("请输入数字："))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 60 <= score <= 79:
    print("C")
elif 40 <= score <= 59:
    print("D")
elif 0 <= score <= 39:
    print("E")
else:
    print("请输入正确的分数")

# 任务13
"""
lst = [4, 6, 1, 7, 2, 9, 3] 
需求：使用冒泡排序，升序排列列表lst
提示：冒泡排序的核心思想是相邻的两个数据进行比较，假设数列A有n个数据，先比较第1个和第2个数据，如果A1 > A2,则交换他们的位置，确保较大的那个数在右侧。接下来比较A2和A3，采用相同的规则，较大的数向右移动，最后会比较An-1 和An的大小，如果An-1 > An，那么交换他们的位置，这时，An是数列中的最大值
"""
lst = [4,6,1,7,2,9,3]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            # 使列表第一个元素一直是最大
            # 依次跟剩下的进行对比
            lst[i],lst[j] = lst[j],lst[i]
print(lst)

