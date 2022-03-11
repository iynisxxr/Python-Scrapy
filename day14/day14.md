# day14

## 一、datetime模块

- 获取当前日期：datetime.datetime.now()
- 获取当前年月日：datetime.date.today()
- 时间戳：datetime.datetime.now().timestamp()
- 当前指定时间：
	- 时：datetime.timedelta(hours=2)
	- 天：datetime.timedelta(days=2)
	- 年：datetime.timedelta(year=2)



## 二、json模块

- 数据类型转字符串：dumps(数据)
- 字符串转回数据类型：loads(数据)



## 三、random模块

- 产生一个随机数：random.randint(1,10）
- 产生给定数据的随机字符：random.sample(range(1,11),6)  # 6是获取的个数
- 获取指定范围内的指定字符：random.randrange(0,100,2)  # 获取0到100的偶数



## 四、re模块

### 1.表达式

- [ ]

	```
	[0123456789]    #表示匹配任意一个数字
	[0-9]   	    #表示匹配任意一个数字
	[yml]   	    #表示匹配'y','m','l'中任意一个字符
	[a-z]   		#表示匹配任意一个小写字符
	[A-Z]   		#表示匹配任意一个大写字符
	[0-9a-zA-Z]		#表示匹配任意一个数字和字母
	[0-9a-zA-Z_]    #表示匹配任意一个数字、字母和下划
	```

- \

	|  \d  | 匹配任何十进制数字                             |
	| :--: | ---------------------------------------------- |
	|  \D  | 与 \d 相反，匹配任何非十进制数字的字符         |
	|  \s  | 匹配任何空白字符（包含空格、换行符、制表符等） |
	|  \S  | 与 \s 相反，匹配任何非空白字符                 |
	|  \w  | 匹配数字、字母和下划线                         |
	|  \W  | 于 \w 相反                                     |

- 边界字符
	- 行首匹配：^
	- 行尾匹配：$

- 匹配多字符
	- 匹配括号内的内容：(xyz)
	- 匹配前一个字符0次或者无限：*
	- 匹配前一个字符1次或者无限次：+
	- 匹配前一个字符0次或者无限次：?
	- 匹配前一个字符m次：{m}
	- 匹配前一个字符m次到n次：{m,n}
	- 匹配1次或者1次(非贪婪模式)：? ?

- 模式
	- 忽略大小写：re.l
	- 多行匹配：re.M
	- . 不受限制：re.S
	- 忽略正则表达式中的空白和#号的注释：re.X



### 2.函数

|  参数   |      意义      |
| :-----: | :------------: |
| pattern |   正则表达式   |
| string  | 要匹配的字符串 |
|  flags  | 模式（可不写） |

- 匹配字符串开始的字符匹配

	- ```python
		re.match(pattern, string, flags)
		# 匹配成功返回对象，否则返回None
		# 使用group(num) 或  groups() 匹配对象函数来获取匹配表达式
		```

- 扫描整个字符串并返回第一个成功的匹配

	- ```python
		re.search(pattern, string, flags)
		# 匹配成功返回对象，否则返回None
		# 使用group(num) 或  groups() 匹配对象函数来获取匹配表达式
		```

- 编译正则表达式，生成一个正则表达式对象

	- ```python
		re.compile(pattern,flags)
		# 供 match() 和 search() 这两个函数使用
		```

- 通过正则表达式所匹配的所有子串，并返回一个列表
	- ```
		findall(string,pos,endpos)
		# match 和 search  是匹配一次 findall 匹配所有
		# 如果没有找到匹配的，则返回空列表
		# pos : 可选参数，指定字符串的起始位置，默认为 0
		# endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度
		```

		