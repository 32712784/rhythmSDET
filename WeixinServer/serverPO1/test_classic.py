# coding=utf-8
import json

import requests
import pytest

# class TesgTag:
#     def __init__(self):
#         self.corpid = "wwc22ed107cba3e3bc"
#         self.secret = "ub7-0vDTcnWFe-EqvxrePEwwOZO7D80S1cgDELhCIR8"
#
#     def get_token(self):
#         token = None
#         url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET"
#         params = {"corpid": self.corpid,"corpsecret": self.corpid}
#         r = requests.get(url, params=params)
#         resp_body = r.json()
#         if r.status_code == 200 and resp_body["errcode"] == 0:
#             token = resp_body["access_token"]
#         return token
#
#     def test_add(self):
#         pass
#
#     def update(self):
#
#         pass

corpid = "wwc22ed107cba3e3bc"
secret = "ub7-0vDTcnWFe-EqvxrePEwwOZO7D80S1cgDELhCIR8"


def test_get_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    params = {"corpid": corpid, "corpsecret": secret}
    r = requests.get(url, params=params)
    resp_body = r.json()
    assert r.status_code == 200
    assert resp_body["errcode"] == 0
    token = resp_body["access_token"]
    return token


def test_get_list():
    token = test_get_token()
    url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
    params = {"access_token": token}
    r = requests.get(url, params=params)
    resp_json = r.json()
    tag = None
    # print(type(resp_json))
    # print(type(json.dumps(resp_json, indent=2)))
    # print(json.dumps(resp_json))
    for tag_group in resp_json["tag_group"]:
        if tag_group["group_name"] == "python15":
            tag = tag_group["tag"]
    print(tag)


def test_tag_update():
    token = test_get_token()
    url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
    params = {"access_token": token}
    data_json = {"id": "etmyPyDAAA5kOxSYXa1qz81Vm9vBXMBA",
                 "name": "tag2",
                 "order": 1
                 }
    r = requests.post(url, json=data_json, params=params)
    resp_json = r.json()
    assert r.status_code == 200
    assert resp_json["errcode"] == 0
    assert resp_json["errmsg"] == "ok"


