# 任务4
a = "abcd"
print(a.upper())

# 任务5
a = "abcd"
print(a.find("cd"))

# 任务6
a = "a,b,c,d"
print(type(a.split(",")))
# <class 'list'>

# 任务7
print("{name}喜欢{fruit}".format(name="李雷",fruit="自己"))

# 任务8
string = "Python is good"
print(string.replace("Python","python"))

# 任务9
string = "python修炼第一期.html"
print(string.split(".")[0])
print(string[0:11])
print(string.strip(".html"))
print(string.replace(".html",""))

# 任务10
string = "this is a book"
print(string.replace("book","apple"))

# 任务11
string = "this is a book"
print(string.startswith("this"))

# 任务12
string = "this is a book"
print(string.endswith("apple"))

# 任务13
string = "This IS a book"
print(string.lower())

# 任务14
string = "This IS a book"
print(string.upper())

# 任务15
string = "this is a book\n"
print(string.strip("\n"))
print("测试换行")

# 任务16
lst = [1,2,3,4,5]
print(len(lst))
print(6 in lst)
print(lst + [6,7,8]) # 合并列表
print(lst * 2) # 列表元素翻倍
print(max(lst)) # 5
print(min(lst)) # 1
print(sum(lst)) # 15
lst.insert(1,10)
print(lst)
lst.append(20)
print(lst)

# 任务17
print("="*20+"任务17"+"="*20)
lst = [2, 5, 6, 7, 8, 9, 2, 9, 9]
lst.append(15)
print(lst)
lst.insert(len(lst)//2,20)
print(lst)
print(lst + [2,5,6])
del lst[3]
print(lst)
print(list(reversed(lst)))
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

# 任务18
dic = { 'python': 95, 'java': 99, 'c': 100 }
print(len(dic)) # 3
dic["java"] = 98
print(dic)
del dic["c"]
print(dic)
dic["php"] = 90
print(dic)
lst = dic.keys()
print(lst)
lst = dic.values()
print(lst)
print("javasript" in dic)
print(sum(dic.values()))
print(max(dic.values()))
print(min(dic.values()))
dic1 = {"c++":97}
dic.update(dic1)
print(dic)

# 任务19
lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]
# 在lst1中，在lst2中
print(set(lst1) & set(lst2))
# 在lst1中，不在lst2中
# 使用 ^ 是输出对称差集：{1，3，6，7，9}
print(set(lst1) - (set(lst2)))
# 两个列表有哪些整数
print(set(lst1) | set(lst2))



