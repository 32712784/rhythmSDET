# coding=utf-8
import json
from mitmproxy import http

def response(flow: http.HTTPFlow):
    # 修改判断条件
    if "quote.json" in  flow.request.pretty_url and "x=" in flow.request.pretty_url:
        resp_json = json.loads(flow.response.content)
        # print(resp_json)
        # 修改json中的数据
        resp_json["data"]["items"][0]["quote"]["name"] = "茅台霍格沃兹"
        resp_json["data"]["items"][1]["quote"]["name"] = resp_json["data"]["items"][1]["quote"]["name"]*2
        resp_json["data"]["items"][2]["quote"]["name"] = ""
        # json格式转换成字符串后，传给响应body
        resp_text = json.dumps(resp_json)
        flow.response.text = resp_text
