### Mysql

```sql
'''
		linux 切换到管理员 sudo -s
		linux 如何知道是否管理员 @前面是root 命令行前头是#
		linux /var/lib/mysql 下面有mysql的文件
		
		关系型数据库
		列-->字段 行-->记录
		
		C/S OR B/S 两种大架构
		RDBMS -client/ -server  
		
		SQL 主要分为
		DOL 数据查询 eg: select
		DML 数据操作 eg: insert, update, delete
		TPL 事务处理	eg: begin transaction, commit, rollback
		DCL 数据控制 eg: grant, revode
		DDL 数据定义 eg: create, drop
		CCL 指针控制 eg: declare cursor
		
		ubuntu安装
		sudo apt-get install mysql-server
		
		ubuntu客户端安装
		sudo apt-get install mysql-client
		
		开启服务
		sudo service mysql start
		
		停止服务
		sudo service mysql stop
		
		重启服务
		sudo service mysql restart
		
		# 显示进程
		linux top 
		linux htop
		linux ps 
		linux ps -aux | more 
		linux ps -aux | grep "mysql"
		
		配置文件目录为 
		/etc/mysql/mysql.cnf
		/etc/mysql/mysql.cnf.d
		
		linux 删除文件 rm 文件名 -r(删除文件夹)f(强制删除)    
'''

 
		## 数据库操作
		
		# 通过mysql client链接mysql server
		mysql -uroot -proot or mysql -uroot -p
		
		# 退出数据库
		exit or quit or control + d

		# 显示时间
		select now();
		
		# 查看所有数据库
		show databases;
		
		# 查看当前数据库版本
		select version();
		
		# 创建数据库名字
		create database my_database;
		create databse charset=utf8;
		
		# 删除数据库
		drop databse `my_database`;
		
		# 查看创建数据库的语句
		show create databse my_database;
		
		# 查看当前用什么表
		select database();
		
		# 切换当前数据库
		use + 数据库名称;
		
		# sql 语句分离
		
----------------------------	

		## 数据表操作
		
		# 展示所有的表
		show tables;
		
		# 创建数据表
		create table xxx (字段 类型 约束[, 字段 类型 约束])
		create table user (id int primary key not null auto_increment, name varchar(30));
		eg1:
		create table user (
      id int primary key not null auto_incrementm,
      name varchar(30)
		);
		eg2:
		create table students(
				id int unsigned primary key not null auto_increment,
        name varchar(30),
        age tinyint unsigned default 0,
        high decimal(5, 2), 
        gender enum("female", "male", "secret") default "secret",
        cls_d int unsigned
		)
		eg3:
		create table classes(
				id int unsigned not null auto_increment primary key,
				name varchar(30) not null
		);
		
		# 查看数据表内部情况
		desc 表名;
		
		# 插入数据
		insert into students values(0, "Roger", 18, 182.8, "male", 0);
		
		# 查询数据
		select * from 数据表名;
		
		# 添加字段/插入字段
		alter table 表名 add birthday datetime
		
		# 修改字段
		alter table 表名 modify birthday date
		
		# 直接更换字段 重命名
		alter table students change birthday birth date default "1900-01-01";
		
		# 删除字段
		alter table students drop high
		
		# 删除数据库
		# 删除数据表
		drop database 数据库名称
		drop table 数据表名称
		
		# 查看创建表的语句
		show create table 表名
		
----------------------------
		
		## CRUD
		
		# 往表里插入数据(全部插入 / 一次插入多行)
		insert into 表名 values(字段, 字段, 字段...);
    # 枚举类型可以使用 从1开始的下标来表示
		insert into 表名 values(..., 1/2/3);
		insert into 表名 vlaues (字段, 字段, 字段) (字段, 字段, 字段);
		
		# 往表里插入数据(部分插入 / 一次插入多行)
		insert into 表名 (列名称, 列名称) values (字段, 字段) (字段, 字段); 
		
		# 更新表内数据
		update 表名 set 列1=值1, 列2=值2 ... where 条件;
		update students set gender = xxx where id = xxx;
		
		# 查询
		select * from 表名;
		select * from 表名 where 条件;
		select 列1 as 别名1, 列2 as 别名2(不能用数字) from 表名 where 条件;
		select 列2 as 别名2(不能用数字), 列1 as 别名1 from 表名 where 条件;
		
		# 删除数据 物理删除
		delete from students where id = 1;
		
		# 逻辑删除
		alter table students add is_delete bit default 0;
		update students set is_delete = 1 where name = "Mary";
		select * from students where is_delete = 1;
		
		# 去重
		select distinct gender from students;

```



#### Query

```sql
		# 条件
		select ... from 表名 where ...
				
				## 精准查询

        # >
        select * from students where age > 18;

        # < 
        select * from students where age < 18;

        # >=
        # <=
        select * from students where ages >= 19;
        select * from students where ages <= 19;

        # =
        select name from students where ages = 19;

        # != or <>
        select * from students where ages != 19;

        # and
        select * from students where age >= 18 and age <= 28;
				select * from students where age >= 18 and gender = "female";
		
        # or
        select * from students where age >= 18 or height >= 180.00;
        
        # not
        # 只会否定后面的第一个条件
        # 选择年龄不超过18的女性
        select * from studentt where not age >= 18 and gender = "female";
        # 选择年龄不超过18并且不是女性
        select * from studentt where not (age >= 18 and gender = "female");
        
        ## 模糊查询
        
        # like
        % 替换1个或多个
        _ 替换1个
        # 查询名字刚好是L开头
        select name from students where name like "L%";
        # 查询名字包含L即可
        select name from students where name like "%L%";
        # 查询名字刚好有3个字符的名字
        select name from students where name like "___";
        # 查询名字至少有2个字符的名字
        select name from students where name like "__%";
        
        # rlike
        select name from students where name like rlike "^J.*";
        select name from students where name like rlike "^J.*L$";
        
        ## 范围查询
        
        # in
        select name, age from students where age = 18 or age = 22;
        select name, age from students where age in (18, 22, 34);
         
        # not in 
        select name, age from students where age not in (21, 22);
        
        # between and  
        select name, age from students where age between 18 and 23; # ->[18, 23
        select * from students where age not between 18 and 34;
        select * from students where not age between 18 and 34;
        # (X) select * from students where age not ( between 18 and 34 );
        
        ## 空判断
        
        # is null
        select * from students where height is null;
        
        # is not null
        select * from students where age is null;
        
		
		# 排序
		
				# order by 单个字段排序 (默认asc /desc)  
				select * from students where (age between 18 and 24) and gender = "male" order by age asc;
				# order by 多个字段 
			 	select * from students where (age between 18 and 24) and gender = "male" order by age asc, id asc;
			 	
			 	select * from students order by age asc, height desc;
				
		# 聚合函数/统计
		
				# count
				select count(*) as "the number of male" from students where gender = "male";
				
				# max
				select max(age) as "the max age of students" from students;
				select max(height) as from students where gender = "female";
				
				# min
				select min(age) as from students where gender = "male";
				
				# sum
				select sum(age) from students;
				
				# avg
				select avg(age) from students;
				select sum(age) / count(*) from students;
				
				# round(数值, 保留位数)
				select round(sum(age)/count(*), 2) from students;
				# 聚合结果只能显示一列
				select round(sum(height)/count(*), 2) from students where gender = "male";
		
		# 分组
		
				# group by
				# 分组完以后 只能取分完组以后数据
				# 对于原表进行判断
				# (X) select name from students group by gender
				# (X) select * from students group by gender
				select gender from students group by gender;
				
				# 计算每种性别里的人数
				select gender, count(*) from students group by gender;
				select gender, avg(age), group_concat(name) from students group by gender;
				
				
				# 计算男性的人数
				select gender, count(*), group_concat(name, "_", age, "_", id) from students where gender = "male" group by gender;
				
				# group_concat
				select gender, group_concat(name) from students where gender = "male" group by gender;
				select gender, count(*), group_concat(name, "_", age, "_", id) from students where gender = "male" group by gender;
				
				# having
				# 对分组结果进行条件判断
				select gender, group_concat(name), avg(age) from students group by gender having avg(age) > 30;
				select gender, group_concat(name) from students group by gender having count(*) > 2;
				
		
		# 分页
		
		# 连接查询
		
		# 自关联
		
		# 子查询
    
    # 
    
    

```

