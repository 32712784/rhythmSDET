# coding=utf-8
from mitmproxy import http
import os

def request(flow: http.HTTPFlow):
    # 修改判断条件
    if "quote.json" in  flow.request.pretty_url:
        # 打开本地json文件
        # with open(r"D:\Python3_workspace\rhythmSDET\MockDemo\quote.json","r",encoding="utf8") as f:
        with open(os.path.abspath(os.path.split(os.path.realpath(__file__))[0]+"/quote.json"),"r",encoding="utf8") as f:
            flow.response = http.HTTPResponse.make(200,f.read(),{"Content-Type": "application/json"})

# mitmdump -p xxxx -s python_path