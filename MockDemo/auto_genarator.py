# -*- coding: utf-8 -*-
import json
from mitmproxy import http

rule = [0,1,2]

# 统计url和访问次数
url_index = {}

def response(flow:http.HTTPFlow):
    url = flow.request.url.split(".json")[0]
    if url not in url_index.keys():
        url_index[url] = 0
    else:
        url_index[url] += 1
    # 根据url访问次数，取余rule，以便每次访问后，翻倍数量不一样
    seed = url_index[url]%len(rule)

    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应body转换为字典
        data = json.loads(flow.response.content)
        # 翻倍数据，每次取值不一样的翻倍数量  !!!对text翻倍后，雪球页面无法显示自选列表！！！
        data_new = json_traval(data,array=rule[seed])
        # 翻倍后的数据，重新传给响应body
        flow.response.text = json.dumps(data_new)

def json_traval(data, array=None, text=1, num=1):
    """
    完成json数据翻倍操作
    :param data: 要翻倍的数据
    :param array: 列表要翻的倍数，默认不翻
    :param text: 字符串要翻的倍数，默认为1，不翻倍
    :param num: 数值要翻的倍数，默认为1，不翻倍
    :return: data_new 翻倍后返回
    """
    data_new = None
    # 如果data是字典，则data_new定义为字典
    if isinstance(data,dict):
        data_new = {}
        # 遍历字典的key，以便进行翻倍
        for k, v in data.items():
            # 对每个key对应的value进行翻倍
            data_new[k] = json_traval(v,array,text,num)

    elif isinstance(data, list):
        data_new = []
        # 如果是列表，遍历列表中的所有元素,并存入新的列表中
        for item in data:
            item_new = json_traval(item, array, text, num)
            # 如果列表为空，则不翻倍，直接返回
            if array is None:
                data_new.append(item_new)
            # 如果array是整数且大于0，则翻倍数据
            elif isinstance(array, int) and array >0:
                for i in range(array):
                    data_new.append(item_new)
            # 为负或者不为整数，不翻倍
            else:
                data_new.append(item_new)
    # 如果data是字符串，判断text是否传入正整数，有则进行字符串和整数相乘
    elif isinstance(data, str) :
        if isinstance(text,int) and text>=0:
            data_new = data * text
        else:
            # 否则如果传入负值或者非正整数的值,原样返回
            data_new = data
    # 如果是传入的data是数值，进行乘积
    elif isinstance(data,int) or isinstance(data, float):
        data_new = data * num

    # 其他类型数据不变，比如布尔值等等
    else:
        data_new = data


    return data_new

# with open(r".\generator.json","r",encoding="utf8") as f:
#     data = json.load(f)
#     print(data)
# print(json_traval(data,1, 2, 2))
