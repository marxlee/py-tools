#!/usr/bin/python3

from urllib import request, parse
import ssl
import re


def fn():
    url = 'https://www.qiushibaike.com/text/page/2/'

    data = {
        'username':"aaa",
        'passwd':"bbb",
    }

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    # 注意编码类型
    parse_data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url=url, data=parse_data, headers=header)
    # ssl 无证书访问
    context = ssl._create_unverified_context()
    # req.add_header()
    resp = request.urlopen(req, context=context)
    rd = resp.read().decode('utf-8')
    print(rd)


    pass


if __name__ == '__main__':

    fn()
    pass