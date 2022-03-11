# day16

## 一、私有属性和方法

### 定义

隐藏的不行被人知道属性，方法，称为封装

### 格式

属性和方法前面添加双下划线

### 注意

属性隐藏起来，并非不让外部使用，而是在使用时得到控制

### 代码示例

```python
class Animal:    
    def __init__(self, name, age):        
        self.__name = name        
        self.__age = age    
    
    def set_age(self, age):        
        if age > 100 or age < 1:            
            raise Exception("年龄范围错误")        
        self.__age = age    
    
    def get_age(self):        
        return self.__age    
    
    def __run(self):        
        print("run")
 
a = Animal('猫', 2)
a.set_age(3)
print(a.get_age())
a.set_age(101)

"""
输出结果：
3
Exception: 年龄范围错误
"""
```



## 二、类属性

### 定义

类可以有自己属性，这个属性不同于实例的属性，类属性属于类，但是可以被实例访问

### 代码实例

```python
class People(object):    
    country = '中国'

p = People()
print(p.country)
p.country = "美国"
print(p.country)

"""
输出结果：
中国
美国
"""
```



## 三、classmethod（类方法）

### 定义

类中的方法都是普通方法，第一个参数是self，这种方法只能被实例调用，如果被classmethod装饰，这个方法就是类方法，可以被类和实例调用

### 使用

在方法前一行添加	@classmethod

且第一个参数默认写成	cls

### 代码实例

```python
class People(object):    
    country = '中国'    
    people = 0        
    
    @classmethod    
    def sing_the_national_anthem(cls):        
        print('唱{country}国歌'.format(country=cls.country))
        
People.sing_the_national_anthem()
p = People()
p.sing_the_national_anthem()

"""
输出结果：
唱中国国歌
唱中国国歌
"""
```



## 四、staticmethod（静态方法）

### 定义

静态方法是类中的函数。静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中

### 使用

在方法前一行添加	@staticmethod

### 代码示例

```python
class People(object):    
    country = '中国'    
    
    @staticmethod    
    def sing_the_national_anthem():        
        print('唱国歌')
        
People.sing_the_national_anthem()
p = People()
p.sing_the_national_anthem()

"""
输出结果：
唱国歌
唱国歌
"""
```



## 五、三种类方法对比

|   名称   |                           定义方法                           |                        权限                        |            调用方法            |
| :------: | :----------------------------------------------------------: | :------------------------------------------------: | :----------------------------: |
| 实例方法 |             第一个参数必须是示例，一般命名为self             | 可以访问实例的属性和方法，也可以访问类的实例和方法 | 一般通过示例调用，类也可以调用 |
|  类方法  | 使用装饰器@classmethod修饰，第一个参数必须是当前的类对象，一般命名为cls |               可以访问类的实例和方法               |      类实例和类都可以调用      |
| 静态方法 |     使用装饰器@staticmethod修饰，参数随意，没有self和cls     |           不可以访问类和实例的属性和方法           |   实例对象和类对象都可以调用   |

