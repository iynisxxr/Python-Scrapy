# day15

一、面向对象 VS 面向过程

|   名称   |                             优点                             |                             缺点                             |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 面向对象 | 解决了程序的扩展性。对某一个对象单独修改，会立刻反映到整个体系中 | 可控性差，无法很精准的预测问题的处理流程与结果，面向对象一旦开始就由对象之间的交互解决问题，无法预测最终结果 |
| 面向过程 |           降低程序的复杂度，顺着执行，堆叠代码即可           |       一套流程就是用来解决一个问题，代码牵一发而动全身       |



二、类

- 声明

	- ```python
		class 类名:
		    pass
		```

- 作用

	- 属性引用：通过 类名.属性 可用查看类中的属性
	- 实例化，即创建对象：通过 对象名 = 类名(参数) 进行实例化

- 补充：

	- ```python
		# 简单案例
		class Cat(): # 尽量使用大驼峰命名法（单词第一个字母大写）
		
		    # 为对象设置初始值的方法————初始化方法(init)
		    # __init__是对象的内置方法，专门用来定义有属性的方法
		    # 
		    def __init__(self,name):
		        print("创建对象会直接调用此方法")
		        # self.name = "Tom" # 此方法导致只有一个名字
		        self.name = name
		
		    # 哪一个对象调用方法，self就是那个对象的引用
		    def eat(self):
		        print(f"{self.name}爱吃鱼")
		    
		    # 在类中，称为方法，不在类中称为函数
		    def drink(self): # 方法必须加上self
		        print("小猫要喝水")
		
		# 创建对象（实例化对象）
		# 当使用类名()的方法时，会自动调用初始化方法__init__
		tom = Cat("Tom")
		'''
		注意：
		tom和toms是引向不同的内存地址，而并非同一个
		'''
		toms = Cat("New_Tom")
		
		# 对象添加属性(不推荐此方式)
		# tom.name = "Tom"
		
		# 调用对象
		tom.eat()
		tom.drink()
		
		# toms.name = "多个Tom"
		toms.eat()
		
		```



三、面向对象的三大特征

- 继承：继承是一种创建新类的方式，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类
	- ```python
		class ParentClass1: #定义父类    
		    pass
		class ParentClass2: #定义父类    
		    pass
		class SubClass1(ParentClass1): #单继承
		    pass
		class SubClass2(ParentClass1,ParentClass2): #多继承   
		    pass
		```

- 抽象：抽取类似或者说比较像的部分

	- ![面向对象-抽象](E:\Typora\Notes\采集\面向对象-抽象.jpg)

	- ![面向对象-继承](E:\Typora\Notes\采集\面向对象-继承.jpg)

	- ```python
		# 简单实例
		"""
		将猫和狗的共同动作：吃、喝 抽象（将相同的行为提取为一个主类，然后通过子类去继承）给父类
		然后猫类和狗类通过继承这个父类，即可拥有父类中吃 和 喝这两个方法
		"""
		class Animal:    
		    
		    def eat(self):        
		        print("%s 吃 " %self.name)   
		        
		    def drink(self):        
		        print ("%s 喝 " %self.name)
		        
		class Cat(Animal):
		    
		    def __init__(self, name):        
		        self.name = name        
		        self.breed = '猫'
		        
		    def climb(self):        
		        print('爬树')
		        
		class Dog(Animal):    
		    
		    def __init__(self, name):        
		        self.name = name
		        self.breed='狗'
		        
		    def look_after_house(self):        
		        print('汪汪叫')
		
		c1 = Cat('小白家的小黑猫')
		c1.eat()
		c2 = Cat('小黑的小白猫')
		c2.drink()
		d1 = Dog('胖子家的小瘦狗')
		d1.eat()
		```



- 派生：子类也可以添加自己新的属性或者在自己这里重新定义这些属性，但是如果重新定义了自己的属性且与父类重名，则新增属性以自己重新定义的为准

	- ```python
		class Animal:    # 父类
		    def __init__(self, name, aggressivity, life_value):
		        self.name = name 					# 名字
		        self.aggressivity = aggressivity 	# 攻击力
		        self.life_value = life_value		# 血
		        
		    def eat(self):        
		            print(f'{self.name}在吃东西')
		
		class Dog(Animal): # 狗类
		    def bite(self, people):       # 咬人
		        people.life_value -= self.aggressivity
		        
		class Person(Animal): # 人类
		    def attack(self, dog):		# 打狗
		        dog.life_value -= self.aggressivity
		        print(f'{dog.name}受到{self.aggressivity}点伤害')
		
		Gai = Person('盖',10,1000)
		er_ha = Dog('二哈',50,1000)
		print(er_ha.life_value)
		Gai.attack(er_ha)
		print(er_ha.life_value)
		
		"""
		输出结果：
		1000
		二哈受到10点伤害
		990
		"""
		```

		

