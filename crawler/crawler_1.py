
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

def multi_url(r_url, w_url):
    req = None
    for i in range(1, 9):
        str = i+'.jpg'
        url = urljoin(r_url, str)
        req = request.Request(url=url, headers=headers)
        context = ssl._create_unverified_context()
        respo = request.urlopen(req, context=context)
        data = respo.read()
        wr_url = urljoin(w_url, str)
        with open(wr_url, 'w+b') as f1:
            f1.write(data)


def single_url(r_url, w_url):
    url = r_url
    req = request.Request(url=url, headers=headers)
    context = ssl._create_unverified_context()
    respo = request.urlopen(req, context=context)
    data = respo.read()
    print(type(data))
    with open(w_url, 'w+b') as f1:
        f1.write(data)



if __name__ == '__main__':
    single_url()
    # multi_url()
    pass


