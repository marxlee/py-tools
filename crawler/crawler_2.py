

from urllib import request
import random
import json

# 摸你请求头

url = r'https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd=%E7%9F%B3%E7%94%B0%E7%BA%AF%E4%B8%80%E6%84%9F%E6%9F%93%E6%96%B0%E5%86%A0&rsv_idx=2&rsv_dl=fyb_n_homepage&hisfilter=1'

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







# 方法体
def print_url(url, header):
    # 设置超时时间处理
    time_out = 1
    req_str = request.Request(url=url, headers=header)
    try:
        resp = request.urlopen(req_str, timeout=time_out)
        data = resp.read().decode()
        print(data)
    except:
        print("超时")
    finally:
        request.urlcleanup()


def print_url_http(url, header):
    '''
    GET
    POST
    PUT
    DELETE
    UPDATE
    HEAD
    OPTIONS
    '''
    json.loads()



    pass



def get_json_val():
    str = data_json_str()
    jd = json.loads(str)
    print(jd['sodar_query_id'])

    # json = data_json()
    # print(json['sodar_query_id'])




def data_json():
    data = {"sodar_query_id":"YcqaXvPrIMSW2QTPjZeQAQ","injector_basename":"sodar2","bg_hash_basename":"r_kJ4x66L0q9ptqPN1EZdQZJVGt7LCWecB4z-4tOz0Y","bg_binary":"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"}
    return data

def data_json_str():
    data = {"sodar_query_id": "YcqaXvPrIMSW2QTPjZeQAQ", "injector_basename": "sodar2",
            "bg_hash_basename": "r_kJ4x66L0q9ptqPN1EZdQZJVGt7LCWecB4z-4tOz0Y",
            "bg_binary": "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"}
    data = json.dumps(data)
    return data

# 读取本地
def load_location():
    with open('../files/json.txt', 'rt') as f:
        text = f.read()
        print(text)
        print(type(text))
        js = json.loads(text)
        print(js['sodar_query_id'])
        pass

# 写入本地
def write_location():
    with open('../files/json.txt', 'rt') as f:
        text = f.read()
        with open('../files/json1.txt', 'w') as f1:
            f1.write(text)

if __name__ == '__main__':
    # print_url(url=url, header=headers)
    # load_location()
    write_location()
    pass