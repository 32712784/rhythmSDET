# coding=utf-8
import json
from datetime import datetime

# import jsonpath
from rhythmSDET.WeixinServer.serverPO1.tag import Tag
import pytest


class TestTag():
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id, tag_name", [
        ["etmyPyDAAA5kOxSYXa1qz81Vm9vBXMBA", "tag1_ABCD"],
        ["etmyPyDAAA5kOxSYXa1qz81Vm9vBXMBA", "tag2_中文"]
    ])
    def test_tag_list(self, tag_id, tag_name):
        tag_name_new = tag_name + "__" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tag.list()
        self.tag.update(tag_id, tag_name_new)
        r = self.tag.list()
        # print(json.dumps(r.json(),indent=2))
        assert r.status_code == 200
        tag_names = [tag["name"] for group_list in r.json()["tag_group"] for tag in group_list["tag"] if tag["id"]==tag_id]
        assert tag_name in tag_names[0]

    # 40071：GroupName或UserTag Name已存在
    @pytest.mark.parametrize("group_name, tag_list", (
            ["groupName2", [{"name": "tag3"}, {"name": "tag2"}]],
    )
                             )
    def test_tag_add(self,group_name, tag_list):
        # group_name = "group_name"
        # tag_list = [{"name":"tag1"},
        #             {"name":"tag2"}]
        # r = self.tag.add(tag_list=tag_list)
        r = self.tag.add_and_detect(group_name, tag_list)
        # print(r.json())

    @pytest.mark.parametrize("tag_names, group_names", (
            [["tag","tag"], ["groupName","groupName"]],
    )
                             )
    # 41017 缺少tagid
    # 40068 无效的tagid
    def test_tag_delete(self,tag_names, group_names):
        self.tag.delete_by_names(tag_names, group_names)

    def test_group_delete(self):
        self.tag.delete_and_detect_group(["123456789"])
