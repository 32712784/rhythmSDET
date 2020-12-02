# coding=utf-8
import requests


class TesgTag:
    def __init__(self):
        self.corpid = "wwc22ed107cba3e3bc"
        self.secret = "ub7-0vDTcnWFe-EqvxrePEwwOZO7D80S1cgDELhCIR8"

    def get_token(self):
        token = None
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET"
        params = {"corpid": self.corpid,"corpsecret": self.corpid}
        r = requests.get(url, params=params)
        resp_body = r.json()
        if r.status_code == 200 and resp_body["errcode"] == 0:
            token = resp_body["access_token"]
        return token

    def add(self):
        pass

    def update(self):

        pass

