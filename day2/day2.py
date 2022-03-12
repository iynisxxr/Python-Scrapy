# 任务4:使用input输入正方形的边长，分别输出正方形的周长和面积
long = int(input("请输入正方形长："))
width = int(input("请输入正方形宽："))
perimeter = (long + width) * 2
area = long * width
print(f"正方形周长为：{perimeter}\n正方形的面积为：{area}")

# 任务5:name="明明" age=26 ，格式化输出"明明今年26岁，喜欢吃菠菜"
name = "小明"
age = 26
print(f"{name}今年{age}岁，喜欢吃菠菜")

# 任务6:10 >20 or 4<10 or 100>= 35  输出对应的结果
print(10 > 20 or 4 < 10 or 100 >= 35) 
# 结果为 True
# or中一个True即为True

# 任务7:判断输入的年龄大于或等于50，输出"你不适合做编程"，否则输出"程序猿欢迎您"
age = input("请输入您的年龄：")
if age >= "50":
    print("你不适合做编程")
else:
    print("程序猿欢迎你")

# 任务8:实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
user = input("请输入您的账号：")
password = input("请输入您的密码：")
if user == "seven" and password == "123":
    print("登录成功")
else:
    print("登录失败")

# 任务9:让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确
num = int(input("请输入数字："))
if num > 66:
    print("结果大了")
elif num < 66:
    print("结果小了")
else:
    print("结果正确")

# 任务10
"""
成绩有ABCDE5个等级，与分数的对应关系如下:
A    90-100
B    80-89
C    60-79
D    40-59
E    0-39
根据输入的成绩输出不同的等级
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

# 练习1
# lis = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48] 
# for i in range(1,len(lis)):
#     for j in range(0,len(lis)):
#         if lis[i] < lis[j]:
#             lis[i],lis[j] = lis[j],lis[i]
# print(lis)
