# vim 编辑器参数设定

```
# 用户目录下: pwd
# /home/user
# 如果你是root用户那么路径
# /root


# 输入一下命令
touch .vimrc

vi .vimrc

# 输入一下内容
# 展示行号, 自动缩进, tab键对应空格数4, 换行对其, 关键字高亮
set nu
syntax on
set ts=4
set expandtab
set autoindent
set ruler
set nohls

```