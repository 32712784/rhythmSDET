# coding=utf-8
import json

import requests

from rhythmSDET.WeixinServer.serverPO1.base_api import BaseApi


class Tag(BaseApi):
    # 尝试不加此初始化方法会怎么样！！
    def __init__(self):
        super().__init__()

    # def get_token(self):
    #     corpid = "wwc22ed107cba3e3bc"
    #     secret = "ub7-0vDTcnWFe-EqvxrePEwwOZO7D80S1cgDELhCIR8"
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    #     params = {"corpid": corpid, "corpsecret": secret}
    #     r = requests.get(url, params=params)
    #     r_json = r.json()
    #     assert r.status_code == 200
    #     # print(json.dumps(r_json,indent=2))
    #     assert r_json["errcode"] == 0
    #     token = r_json["access_token"]
    #     # print(token)
    #     return token

    def list(self):
        data = {
            "method": "GET",
            "url" : "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {"access_token": self.token}
        }
        r = self.send(data)
        # r = requests.get(url, params=params)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        # 返回整个响应，以便验证异常场景，响应不为200的情况
        return r

    def add(self, group_name=None, tag_list=None, **kwargs):
        """
        添加联系人接口
        :param group_name:
        :param tag_list:
        :param kwargs: 用于传"group_id": "GROUP_ID","order": 1,
        :return:
        """
        if group_name == None:
            group_name = ""
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {"group_name": group_name,
                     "tag": tag_list,
                     **kwargs
                     }
        }
        r = self.send(data)
        # r = requests.post(url, json=data_json, params=params)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        # 返回整个响应，以便验证异常场景，响应不为200的情况
        return r

    def find_tag_by_group_name(self, group_name, tag_list):
        """
        通过group_name查询对应的tag_name是否存，存在则添加到列表中，提供给删除接口
        :param group_name:
        :param tag_list:
        :return:
        """
        # [tag["name"] for tag in tag_list] 得到["tag2","tag3"]
        tags = [tag["name"] for tag in tag_list]
        isExistTags_id = []
        tag_group = self.list().json()["tag_group"]
        for group in tag_group:
            if group["group_name"] == group_name:
                tag_list_info = group["tag"]
                for tag in tag_list_info:
                    # 如果group_name下对应的tag已经存在，则添加到列表中，提供给删除接口
                    if tag["name"] in tags:
                        isExistTags_id.append(tag["id"])
        print(isExistTags_id)
        return isExistTags_id

    def find_group_id_by_group_name(self, group_name):
        """
        查询group_name对应的id，提供给删除方法做入参
        :param group_name: 列表，查询多个标签组名
        :return: 列表，返回标签组id列表
        """
        tag_group = self.list().json()["tag_group"]
        group_ids = []
        for group in tag_group:
            if group["group_name"] in group_name:
                group_ids.append(group["group_id"])
        return group_ids

    def find_tag_id_by_tag_name(self, tag_name):
        """
        查询tag_name对应的id，提供给删除方法做入参
        :param tag_name: 列表，查询多个标签名
        :return: 列表，返回标签id列表
        """
        tag_group = self.list().json()["tag_group"]
        tag_ids = []
        for group in tag_group:
            for tag in group["tag"]:
                if tag["name"] in tag_name:
                    tag_ids.append(tag["id"])
        return tag_ids

    # 查找groupid是否存
    def is_group_id_exist(self, group_id):
        group_ids=[]
        group_ids = [group["group_id"] for group in self.list().json()["tag_group"]]
        if group_id in group_ids:
            return True
        else:
            print(f"{group_id} not in group")
            return False

    # 查找tagid是否存
    def is_tag_id_exist(self, tag_id):
        tag_ids = [tag["id"] for group in self.list().json()["tag_group"] for tag in group["tag"]]
        if tag_id in tag_ids:
            return True
        else:
            print(f"{tag_id} not in group")
            return False


    # 添加并查数据是否存在，存在则先删除数据，检查group和检查tag，group不存在重复，如果重复接口会新增groupname和tag
    # group如果存在相同，则新增tag，tag相同则报错，group如果不同，则直接增加group和tag
    def add_and_detect(self, group_name, tag_list, **kwargs):
        r = self.add(group_name=group_name, tag_list=tag_list)
        if r.json()["errcode"] == 40071:
            # 判断是哪个tag存在，如果对存在的tag获取其id并删除
            isExistList = self.find_tag_by_group_name(group_name, tag_list)
            print(isExistList)
            # 对存在的tag进行删除后，重新进行add添加
            self.delete_tag(isExistList)
            resp = self.add(group_name=group_name, tag_list=tag_list, **kwargs)
            return resp
        else:
            return r

    # id是标签或标签组的id
    def update(self, id, name):
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.token},
            "json": {"id": id,
                     "name": name,
                     }
        }
        r = self.send(data)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        # 返回整个响应，以便验证异常场景，响应不为200的情况
        return r

    # 通过传入tag或者group name来进行删除
    def delete_by_names(self, tag_names=None, group_names=None):
        """
        通过tag或者group name列表来进行删除
        :param tag_names: tag名列表，如["tag1","tag2"]
        :param group_names: group名列表，如["tempGroup1","tempGroup2"]
        :return:
        """
        # data_json = {
        #     "tag_id": [
        #         "TAG_ID_1",
        #         "TAG_ID_2"
        #     ],
        #     "group_id": [
        #         "GROUP_ID_1",
        #         "GROUP_ID_2"
        #     ]
        # }
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        params = {"access_token": self.token}
        tag_ids, group_ids = [],[]
        if tag_names != None:
            tag_ids = self.find_tag_id_by_tag_name(tag_names)
            print("tag_ids:")
            print(tag_ids)
        if group_names != None:
            group_ids = self.find_group_id_by_group_name(group_names)
            print("group_ids:")
            print(group_ids)
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {"tag_id": tag_ids,
                     "group_id": group_ids,
                     }
        }
        # data_json = {"tag_id": tag_ids,
        #              "group_id": group_ids,
        #              }
        # r = requests.post(url, json=data_json, params=params)
        r = self.send(data)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        return r

    def delete_tag(self, tag_id):
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {"tag_id": tag_id,
                     }
        }
        r = self.send(data)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        return r

    def delete_group(self, group_id):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        # params = {"access_token": self.token}
        # data_json = {"group_id": group_id,
        #              }
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {"group_id": group_id,
                     }
        }
        # r = requests.post(url, json=data_json, params=params)
        r = self.send(data)
        r_json = r.json()
        # 字典格式转换为json格式(字符串)
        print(json.dumps(r_json, indent=2))
        return r

    def delete_and_detect_group(self, group_ids):
        detect_group_ids = []
        r = self.delete_group(group_ids)
        # 40068 group_id不存在
        if r.json()["errcode"] == 40068:
            for i, group_id in enumerate(group_ids):
                if not self.is_group_id_exist(group_id):
                    # 添加group_name不同的组名，否则如果第二次组名相同，会删除第一次的组，但是第一次group_id已经返回并添加到detect_group_ids，后面再删除时，又会找不到id
                    re = self.add_and_detect(f"tempGroup{i}", [{"name": f"tempTag{i}"}])
                    detect_group_ids.append(re.json()["tag_group"]["group_id"])
                else:
                    detect_group_ids.append(group_id)
            resp = self.delete_group(detect_group_ids)
            return resp
        else:
            return r
