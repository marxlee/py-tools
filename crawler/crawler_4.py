import time
from urllib import request, parse
import random
import ssl
import re
from collections import deque







def get_url(url):
    # 代理列表
    agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',

    ]

    # 头信息
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

    }

    # 随机代理
    agent = random.choice(agent_list)
    headers['User-Agent'] = agent


    req = request.Request(url=url, headers=headers)

    context = ssl._create_unverified_context()

    respo = request.urlopen(req, context=context)
    # 清理
    request.urlcleanup()
    # 整页读取
    data = respo.read().decode('utf-8')
    # print(data)
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote">'
    regix = re.compile(pat, re.S)
    s = regix.findall(data)
    print(len(s))
    # return s


    with open('../files/糗事_1.txt', 'wt') as f:
        for div in s:
            re_com = re.compile(r'<h2>(.*?)</h2>', re.S)
            name = re_com.findall(div)
            # print(re.split(r'\n*', '', name[0]))
            re_com = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
            det = re_com.findall(div)
            # print(det[0])
            f.write(name[0] + det[0])




def post_url(url):
    # 代理列表
    agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    ]

    # 头信息
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

    }

    data = {
        'username': "aaa",
        'passwd': "bbb",
    }


    # 随机代理
    agent = random.choice(agent_list)
    headers['User-Agent'] = agent

    # 注意编码类型
    parse_data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url=url, data=parse_data, headers=headers)
    # ssl 无证书访问
    context = ssl._create_unverified_context()
    # req.add_header()
    resp = request.urlopen(req, context=context)
    rd = resp.read().decode('utf-8')
    print(rd)
    pass


def dequeue(url):

    queue = deque()

    queue.append(url)
    queue.append(url + "dlkfjsldf")

    print(len(queue))
    print(queue.popleft())


if __name__ == '__main__':
    url = r'https://www.qiushibaike.com/text/page/2/'
    # get_url(url)
    # print(len(conx))
    dequeue(url)
    pass
