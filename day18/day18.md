# day18

## 一、数据库

### 概述

数据库就是存储数据的仓库，其本质是一个文件系统，数据按照特定的格式将数据存储起来，用户可以对数据库中的数据进行增加，修改，删除及查询操作

### 数据库管理系统

一种操作和管理数据库的大型软件，用于建立、使用和维护数据库（存储、维护和管理数据的集合【容器】），对数据库进行统一管理和控制，以保证数据库的安全性和完整性。用户通过数据库管理系统访问数据库中表内的数据。例如：Mysql、Oracle、SQLServer

### 数据库表

数据库中最频繁提到的一个概念就是“表”。其实，“表”就是人为地总结出来的、用以描述一类事物的一组描述信息，包括  1个或多个方面的信息。比如人的描述信息可以包括（姓名、年龄、职业）等

### 数据表

根据表字段所规定的数据类型，我们可以向其中填入一条条的数据，而表中的每条数据类似类的实例对象。



## 二、SQL

### 概述

一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统。sql 语句就是对数据库进行操作的一种语言。

### 分类

数据定义语言DDL：create、alter、drop

数据操作语言DML：insert、delete、update

数据控制语言DCL：定义数据库访问权限和安全级别，创建用户

数据查询语言DQL：select、from、where

### 通用语法

MySQL数据库的SQL语句不区分大小写，以分号结尾，例如：SELECT * FROM user；

### 常用数据类型

|  类型   |           描述           |
| :-----: | :----------------------: |
|   int   |           整型           |
| double  |          浮点型          |
| varchar |         字符串型         |
|  date   | 日期类型，格式yyyy-MM-dd |



## 三、SQL数据库

### 创建数据库

```sql
create database 数据库名;
create database if not exists 数据库名;		-- 不存在则创建
```

### 查看数据库

```sql
show datables;
```

### 查看某个数据库的定义信息

```sql
show create database 数据库名;
```

### 删除数据库

```sql
drop database 数据库名称;
```

### 切换数据库

```sql
use 数据库名;
```



## 四、SQL表

### 创建表

```sql
create table 表名(
    字段名 类型(长度) 约束,   
    字段名 类型(长度) 约束);
```

### 删除表

```sql
drop table 表名;
```

### 主键约束

```sql
-- 1.在创建表时创建主键
CREATE TABLE 表名(    
    id int primary key,    
    ....)

-- 2.在表创建后指定主键
CREATE TABLE 表名(    
    id int,    
    ....,    
    primary key(id));
```

### 删除主键

```sql
alter table 表名 drop primary key;
```

### 查看表

```sql
show tables;
```

### 查看表结构

```sql
desc 表名;
```

### 修改某列为自增主键modify

```sql
alter TABLE 表明 modify 字段 类型 primary key auto_incremen;
```

### 添加列

```sql
alter table 表名 add 列名 列类型;
```

### 删除列

```sql
alter TABLE 表名 DROP 列名;
```

### 修改表名

```sql
RENAME TABLE 表名 TO 新表名;
```



## 五、作业语句

### 查询表内容

```sql
select * from emp;
```

### 修改员工薪水

```sql
update emp set salary=5000.00 where salary=10000.00; -- 将工资改为5000
```

### 修改zhangsan的薪水

```sql
update emp set salary=3000.00 where name = 'zhangsan'; -- 将zhangsan改为3000
```

### 将lisi修改薪水为3000，性别改为女性

```sql
update emp set salary=4000.00,gender='female' where name = 'lisi';
```

### 将男性薪水+1000

```sql
update emp set salary=salary+1000.00 where gender = 'male';
```

### 删除zhangsan的记录

```sql
delete from emp where name="zhangsan";
```

### 删除全部记录

```sql
truncate table emp;
```



## 六、书写、执行顺序

### 查询语句的书写顺序

```sql
select – from- where- group by- having- order by-limit
```

### 查询语句的执行顺序

```sql
from - where -group by - having - select - order by-limit
```

