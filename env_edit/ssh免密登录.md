# ssh 免密登录

```
# 首先, local机器下生成ssh-key, 回到登录用户目录下


# 接下来, 三次回车
ssh-keygen -t rsa -C "mail@gmail.com"

# 进入 .ssh文件夹
cd ~/.ssh

# ls 包含 id_rsa.pub, id_rsa 文件
ls

# 将ssh 秘钥发送到目标机器, 接着输入登录密码
ssh-copy-id root@ip

# 登录目标机器查看
cd ~/.ssh/authorized_keys

# 查看公钥id_rsa.pub是否已经添加到这里authorized_keys
cat authorized_keys

# 登录
ssh root@ip

```



