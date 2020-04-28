
import time
from urllib import request
from urllib.parse import urljoin

import random
import ssl


ran_int = random.randint(60, 60*5)
print(ran_int)
# time.sleep()
# respo = req.urlopen('https://meiban.gome.com.cn/office/api/clockOn/addJson/10303777/70B1027660E34270-B1BB-643B8F325028_1572920783000/0/0/1')

# 代理列表
agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
]


#头信息
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

}

# 随机代理
agent = random.choice(agent_list)
headers['User-Agent'] = agent

# url = r'http://www.xiaoyuezhang.com/index.html'
# url = r'http://www.redspite.com/cv'
def multi_url():
    req = None
    for i in range(1, 9):
        url_s = ('http://www.xiaoyuezhang.com/image/0%d.jpg' % i)
        print(url_s)
        url = url_s
        req = request.Request(url=url, headers=headers)
        context = ssl._create_unverified_context()
        respo = request.urlopen(req, context=context)
        data = respo.read()
        print(type(data))
        # print(data)
        w_url = ('../dist/file/image/0%d.jpg' % i)
        with open(w_url, 'w+b') as f1:
            f1.write(data)

# services-bg.jpg

def single_url():
    file_name = 'achivements-bg.jpg'
    url_s = 'http://www.xiaoyuezhang.com/image/'
    fill_url = urljoin(url_s, file_name)
    print(fill_url)
    url = fill_url
    req = request.Request(url=url, headers=headers)
    context = ssl._create_unverified_context()
    respo = request.urlopen(req, context=context)
    data = respo.read()
    print(type(data))
    # print(data)
    w_url = '../dist/file/image/' + file_name
    with open(w_url, 'w+b') as f1:
        f1.write(data)


# 整页读取
# data = respo.read().decode('utf-8')
# print(data)

# data = respo.readlines()
# print(data)
# with open('../dist/file/image/', 'wr') as f1:
#     f1.write(data)

# 多行读取
# datas = respo.readlines()
# print(datas)


'''
# 解码url中的编码字段, 转义成为中文
req.unquote(url)

# 编码url中的中文
req.quote(url)




'''


# url = r'https://www.qiushibaike.com/text/page/2/'
# request.urlopen(url)
# new_url = request.quote(url)
# print(new_url)
# new_url = request.unquote(new_url)
# print(new_url)

# 写入文件
# request.urlretrieve(url=url, filename=r'/Users/libinbin/tmp/workspace_pycharm/MachineLearn/python-baseline/base1/files/baidu_html.html')
# 清理缓存
# request.urlcleanup()



if __name__ == '__main__':
    single_url()
    # multi_url()
    pass


