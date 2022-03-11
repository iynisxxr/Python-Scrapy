# day13

## 一、time模块

- 获取当前时间戳：time.time()
- 获取时间戳元组：time.localtime(time.time())
- 获取日常使用的时间格式：time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
- 线程推迟指代的时间运行，单位为秒：time.sleep(1)



## 二、random模块

- 获取指定数字之间的随机数：random.randrange(1,10）
- 获取一个随机浮点数：random.random() 
- 从多个字符中获取指定数量的随机字符：random.sample(range(1,10),3)

