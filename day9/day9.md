# day9

> 一、复习

- 语法错误：

	- 中文引号
	- 缩进
	- 少冒号
	- 少引号
	- 数字开头命名的变量名或函数名
	- range函数

- 异常错误：

	- 0不能做分母
	- 类型不同不能进行运算
	- 函数外调用函数内部的变量

- 捕获异常：

	- ```python
		try:
			检测的代码块
		except Exception as e:
			print(e)
		finally:
		   无论错误与否，都会执行该代码块
		```

- 抛出异常：
	- raise 抛出异常



> 二、进制和符文编码

- 二进制与十进制的转换

- 符文编码
	- ASCII
	- GB2312
	- GBK
	- Unicode
	- UTF-8
	
- 其他

- ASCII码、GBK、Unicode和utf-8之间的关系

	- ASCII码：美国制定的字符编码，规定了128个字符的编码
	- GBK：ASCII编码不支持中文，只能重新定义了规则来支持中文
	- Unicode：国际标准化组织解决所有国家的编码问题的编码方案
	- utf-8：Unicode比较浪费网络带宽和硬盘，在Unicode的基础上，定义了一套编码规则
	- 关系：Unicode通过编码可以得到UTF-8和GBK，UTF-8和GBK也可以通过解码得到Unicode，但GBK和UTF-8之间无法直接转换，只能转换到Unicode后再转到另一编码.

	> 三、文件操作

- GBK 转 UTF8（通过Unicode做桥梁）

	- ```python
		# 编码：
		my_str = "联想"
		new_str = my_str.encode("UTF-8")
		print(new_str)
		# 输出结果：b'\xe8\x81\x94\xe6\x83\xb3'
		```

- 文件打开模式
	- r ：只读
	- w ：创建，存在则覆盖
	- a ：追加
	- wb：二进制流

- 操作方法
	- 读取整个文件：f.read()
	- 读取一行：f.readline()
	- 写入数据：f.write
	- 关闭文件：f.close()

