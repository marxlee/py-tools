## 安装 mysql


```

# 安装完成后登陆, 添加新用户
yum install -y mariadb-service mariadb

# 启动MariaDB
systemctl start mariadb.service 

# 停止MariaDB
systemctl stop mariadb 

# 重启MariaDB
systemctl restart mariadb 

# 设置开机启动
systemctl enable mariadb 

# 取消开机启动
systemctl disable mariadb

# 查阅版本号
mysqladmin --version

# 设置新密码
mysqladmin -u root password "root";

# 登录mariaDB(可以使用mysql)
mysql -u root -p root

# 创建新的用户 以下为sql语句
show databases;
use mysql;

# 需要注意的是, 删除里边host: localhost的数据, 防止你的权限出现问题
insert into mysql.user(Host,User,Password) values('localhost','hadoop',password('hadoop'));

# 添加用户访问权限
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'hadoop'@'%' IDENTIFIED BY 'hadoop' WITH GRANT OPTION;
flush privileges;

```