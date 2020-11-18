# coding=utf-8
import importlib
import yaml

from rhythmSDET.Frame1 import hello
# path,module, func,step
def test_parse_yaml():
    with open("./temp123.yaml") as f:
        datas = yaml.load(f, Loader=yaml.FullLoader)
        # datas = {'test_xxx': [{'hello.a': []}, {'print': ['abcde']}, {'re.search': ['.*', 'xxxx']}, {'save': ['temp']}, {'print': ['$(temp)']}]}
        # print(datas)
        for casename in datas.keys():
            if casename.startswith("test_"):
                print(f"{casename}是标准用例！！")
                # datas[casename] =[{'rhythmSDET.Frame1.hello.test_a1': [1, 2]}, {'print': ['abcde']}, {'re.search': ['.*', 'xxxx']}, {'save': ['temp']}, {'print': ['$(temp)']}]
                # print(datas[casename])
                for step in datas[casename]:
                    for mathod,params in step.items():
                        # 如果包含. 说明是导入模块
                        if "." in mathod:
                            mathod_handle(mathod,params)
                        elif mathod == "print":
                            # 全局变量设置
                            if "$" in params:
                                pass
                            else:
                                print(*params)
                            # 保存全局变量
                        elif mathod == "save":
                            pass
                        else:
                            print(f"{mathod}是未定义的方法！！")
            else:
                print(f"{casename}不是标准用例！！")

# 用于动态导入模块和方法
def mathod_handle(mathod,params):
    # list1 = ['rhythmSDET', 'Frame1', 'hello', 'a']
    list1 = mathod.split(".")
    # list2 = rhythmSDET.Frame1.hello
    list2 = ".".join(list1[0:-1])
    # list3 = test_a1
    list3 = list1[-1]
    main = importlib.import_module(list2)
    # 如果入参不为0，params是list传入动态调用函数作为参数
    if len(params) != 0:
        if hasattr(main, list3):
            # 得到：getattr(main, test_b1)(1, 2)
            getattr(main, list3)(*params)
            # print(getattr(main, list3)(*params))
            print(f"{list2}.{list3}({params})")
    else:
        # 动态导入，执行无参数方法
        if hasattr(main, list3):
            getattr(main, list3)()

def test_parse(module,fun,step):
    # fun = [{'print': [1234]}, {'str': 'a+b+c+d'}]
    for steps in fun:
        for k in steps:
            if k == step:
                main = importlib.import_module(module)
                getattr(main, k)(steps[k])


def test_temp():
    # parse_yaml("./temp123.yaml","hello","test_a", "")
    # 动态导入的两种方式：
    # main = importlib.import_module("rhythmSDET.Frame1.hello")
    main = importlib.import_module(".hello","rhythmSDET.Frame1")
    # 正常调用
    main.test_a1(1,2)
    # 判断动态导入的hello模块下是否有a函数，有则返回True
    if hasattr(main, "test_a1"):
        # 判断动态导入的模块hello下有a函数，则通过getattr()方法动态执行该函数，反射调用
        getattr(main, "test_b1")(3,5)