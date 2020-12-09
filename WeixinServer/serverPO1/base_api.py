# coding=utf-8
import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = "wwc22ed107cba3e3bc"
        corpsecret = "ub7-0vDTcnWFe-EqvxrePEwwOZO7D80S1cgDELhCIR8"
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        r = self.send(data)
        r_json = r.json()
        assert r.status_code == 200
        # print(json.dumps(r_json,indent=2))
        assert r_json["errcode"] == 0
        token = r_json["access_token"]
        # print(token)
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(),indent=2))
        return r
