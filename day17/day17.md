# day17

## 二、面向对象中的继承

### 定义

继承是一种创建新类的方式，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类

### 使用

通过在类名后添加（父类名）来继承父类的属性和方法

### 多继承的注意事项

1.如果子类和父类有相同的方法，就会调用子类中的方法，否则调用父类的方法

2.Python会根据 MRO(method resolution order) 方法解析顺序列表进行查找。采用从左至右的深度优先遍历，不是直接查找父类。但是如果遍历中出现重复的类，只保留最后一个。

### 代码实例

```python
class ParentClass1: #定义父类    
    pass
class ParentClass2: #定义父类    
    pass
class SubClass1(ParentClass1): #单继承
    pass
class SubClass2(ParentClass1,ParentClass2): #多继承   
    pass

# 理解多继承
class A(object):    
    def test(self):        
        print('A test...')

class B(A):    
    def test(self):        
        super().test()        
        print('B test...')
        
class C(A):    
    def test(self):        
        super().test()        
        print('C test...')
        
class D(B,C):    
    def test(self):        
        super().test()        
        C.test(self)        
        print('D test...')

print(D.__mro__)
d = D()
d.test()

"""
输出结果：
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
A test...
C test...
B test...
A test...
C test...
D test...
"""
```

### 其他

#### 派生方法

子类中定义了和父类中相同的方法，我们叫做方法的复写（派生方法）

#### 派生属性

子类也可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了(属性的覆盖)

#### 问题

继承父类后，子类的初始化方法以及派生方法，会覆盖父类的初始化方法

#### 解决

使用super(本类类名,self)调用父类的方法



