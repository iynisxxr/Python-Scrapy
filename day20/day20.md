# day20

## 一、多表查询

### 1.合并结果集

#### 作用

将两个select语句的查询结果合并到一起

#### 用法

```sql
-- UNION：去除重复记录
SELECT * FROM T1 UNION SELECT * FROM T2;
-- UNION ALL：不去除重复记录
SELECT * FROM T1 UNION ALL SELECT * FROM T2;
```



### 2.交叉连接（不常用）

#### 作用

结果集为连接的两个表中所有数据行的乘积，即：

结果集的 第一行 = 第一个表中第一行 + 第二个表中第一行

结果集的 第二行 = 第一个表中第一行 + 第二个表中第二行

以此类推

交叉连接的行数 = 第一个表的行数 * 第二个表的行数

#### 用法

```sql
SELECT * FROM T1,T2;
```



### 3.内连接（常用）

#### 作用

得到两张表中同时符合某种条件的数据记录的组合

#### 用法

```sql
-- 得到T1和T2中拥有共同的ID的结果集
SELECT * 
	FROM T1 
		INNER JOIN T2 
			ON T1.ID = T2.ID;

-- 得到T1和T2中拥有共同的ID,但除了第一位ID的结果集
SELECT * 
	FROM T1 
		INNER JOIN T2 
			ON T1.ID > T2.ID;
```



### 4.外连接

- #### 左外连接

	- ##### 作用

		- 查询出两表中同时符合条件的记录组合，同时还会将"left  join"左侧表中的不符合条件的记录同时展示出来

	- ##### 用法

		- ```sql
			SELECT * FROM T1 left JOIN T2 ON T1.id = T2.id;
			```

	#### 右外连接

	- ##### 作用

		- 查询出两表中同时符合条件的记录组合，同时还会将"right  join"右侧表中的不符合条件的记录同时展示出来

	- ##### 用法

		- ```sql
			SELECT * FROM T1 RIGHT JOIN T2 ON T1.id = T2.id;
			```

			

### 5.子查询（套娃）

#### 作用

用于查询某些条件中大于表中某个值

#### 用法

```sql
-- 用法：在select中嵌套select即称为子查询
-- 查询工资大于张辉的员工
SELECT * 
	FROM emp 
		WHERE sal > (SELECT sal FROM emp WHERE ename='张辉')
```



## 二、运算符

### 1.ANY

#### 作用

ANY修饰的语句，有一个值满足条件即可

即：a大于子查询中的任意一个，等同于a大于子查询的最小值即可

#### 用法

```sql
SELECT * FROM A WHERE a > ANY(SELECT * From s);
```



### 2.SOME

语句some是any的别名，用法相同

```sql
select s1 from t1 where s1 <> any (select s1 from t2);
select s1 from t1 where s1 <> some (select s1 from t2);
-- 其中 ！= 和 <> 两者都是不等于的意思，前者是以前sql标准，<>是现在的标准
```



### 3.ALL

#### 作用

对于子查询返回的列中的所有值，需要全部满足条件

#### 用法

```sql
select s1 from t1 where s1 > all(select s1 from t2);
```



### 4.NOT IN

语句not in 是 “<>all”的别名，用法相同

```sql
select s1 from t1 where s1 = any (select s1 from t2);
select s1 from t1 where s1 in (select s1 from t2);
```



### 5.比较

|       |  ANY   |  SOME  |  ALL   |
| :---: | :----: | :----: | :----: |
| >,>=  | 最小值 | 最小值 | 最大值 |
| <,<=  | 最大值 | 最大值 | 最小值 |
|   =   | 任意值 | 任意值 |        |
| !=,<> |        |        | 任意值 |

