# nginx部署静态页网站

```
yum install -y nginx

# 启动
systemctl start nginx

# 停止
systemctl stop nginx

# 重启
systemctl restart nginx

# 状态
systemctl status nginx

# 修改nginx配置重定向到静态页路径
# 使用yum 安装的nginx配置文件如下
vi /etc/nginx/nginx.conf

# 修改位置
http{} --> server --> root 对应到nginx代理的目录


# 查看nginx端口信息
ps -ef | grep nginx


```




