# coding=utf-8
# test_xxx：仿照 pytest ，文本解析
# hello.a：
# 动态导入：c = importlib.import_module(“hello”)
# 反射： getattr(c, ‘a’)()
# re.search：导入特定包下面的模块tmp = “a.b.c.d.f”.split(".")
# save： globals()[“a”] = 101 ，print(globals()[“a”])
# [$(tmp)]：
# 怎么取到 tmp：globals()[‘tmp’]
# 怎么把 string 当成 python 命令调用： a = 1 ; print(eval(“a”))
import yaml


class TestMain:
    # 解析yaml文件,并且将数据返回
    def load_data(self):
        with open("./tmp.yaml", encoding="utf-8") as f:
            datas = yaml.safe_load(f)
            # print(datas)
        return datas

    # 处理yaml中的数据
    def handle_datas(self, datas: dict):
        # 1.先取到字典所有的key
        # 2.然后判断key是不是以test开头,如果是，执行case，如果不是，不执行
        for key in datas.keys():
            # print(key)
            if key.startswith("test_"):
                # print(f"测试用例的名称是：{key}")
                # print(f"测试用例的数据是：{datas[key]}")
                tmp = datas[key]
                for i in range(0, len(tmp)):
                    for key1 in tmp[i].keys():
                        if key1 == "print":
                            if "$" in tmp[i][key1]:
                                print(f"要调用handle_value函数处理这个东西{tmp[i][key1]}")
                                self.handle_value(value=tmp[i][key1])
                            else:
                                print(f"key = print对应的值是{tmp[i][key1]}")
                        elif key1 == "save":
                            print("调用save函数把内容存储到全局变量中")
                            # self.save(tmp=tmp[i][key1])
                            # tt = str(tmp[i][key1]).replace("[|]|'", "")
                            tt = str(tmp[i][key1])
                            dict_a = {tt: globals()["result"]}
                            print("*************")
                            print(dict_a)
                            print(type(dict_a))
                            print("*************")
                            self.save(tmp=dict_a)
                        elif "." in key1:
                            # 动态导入和反射
                            t = key1.split('.')
                            print(f"模块名是{t[0]},函数名是{t[-1]}")
                            count = __import__(t[0])
                            f = getattr(count, t[-1], None)
                            globals()["result"] = f(*tmp[i][key1])
                            # if len(tmp[i][key1]) != 0:
                            #     # 将函数执行的结果也存储到全局变量中，传递一个字典，key是save后面的变量名，值是函数执行的结果
                            #     tt = str(tmp[i][key1])
                            #     dict_a = {tt:f(*tmp[i][key1])}
                            #     print("*************")
                            #     print(dict_a)
                            #     print(type(dict_a))
                            #     print("*************")
                            #     self.save(tmp=dict_a)
                            # else:
                            #     f(*tmp[i][key1])
                        else:
                            print(f"这个key{key}不特殊，一会看怎么处理")

            else:
                print(f"{key}不是测试用例，不执行")

    # 动态导入+反射
    # 处理带有$的数据,输出$后面的变量的值
    # print：$(tmp)  value=$(tmp)
    def handle_value(self, value):
        # t = "abcd"
        # globals()["str_a"] = "$(t)"
        print("我是调用了函数处理带有$的全局变量")
        globals()["str_a"] = value
        globals()["str_b"] = globals()["str_a"].replace("$", '')
        print(eval(globals()["str_b"]))

    def save(self, tmp: dict):
        print("我是调用了save函数")
        print(tmp)
        print(type(tmp))
        for key in tmp.keys():
            globals()[key] = tmp[key]

        return globals()[key]

    def test_main(self):
        # self.load_data()
        self.handle_datas(datas=self.load_data())
        print(globals().keys())
        print(globals()["tmp_value"])