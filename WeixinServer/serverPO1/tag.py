# coding=utf-8
import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = "wwc22ed107cba3e3bc"
        secret = "ub7-0vDTcnWFe-EqvxrePEwwOZO7D80S1cgDELhCIR8"
        token = None
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET"
        params = {"corpid": corpid, "corpsecret": secret}
        r = requests.get(url, params=params)
        r_json = r.json()
        assert r.status_code == 200
        assert r_json["errcode"] == 0
        token = r_json["access_token"]
        return token

    def add(self):
        pass

    def list(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {"access_token": self.token}
        r = requests.get(url, params=params)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        # 返回整个响应，以便验证异常场景，响应不为200的情况
        return r

    def update(self, id, name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
        params = {"access_token": self.token}
        data_json = {"id": id,
                     "name": name,
                     }
        r = requests.post(url, json=data_json, params=params)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        # 返回整个响应，以便验证异常场景，响应不为200的情况
        return r
