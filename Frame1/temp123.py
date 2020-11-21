# coding=utf-8
import importlib
import yaml

from rhythmSDET.Frame1 import hello
# path,module, func,step
def parse_yaml(path,globalval=None):
    with open(path) as f:
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
                            # 如果字典的key的list[0]包含$，则是全局变量。step={'print': ['$(temp)']}，params=['$(temp)'],用params[0]获取字符串
                            if "$" in params[0]:
                                param = params[0]
                                globaltem = use_global_var(param)
                                print(f"{param}={globaltem}")
                            else:
                                # print(*params)
                                print("打印："+"".join(params))
                                pass
                            # 保存全局变量
                        elif mathod == "save":
                            key = params[0]
                            sava(key,globalval)
                        else:
                            print(f"{mathod}是未定义的方法！！")
            else:
                print(f"{casename}不是标准用例！！")

# 用于保存全局变量
def sava(key,value):
    globals()[key] = value
    result = globals()[key]
    print(f"save：【{result}】已存入全局变量{key}中")
    return result

# 使用全局变量
def use_global_var(param):
    key = param.replace("$(","").replace(")","")
    # 把 string 当成 python 命令调用： a = 1 ; print(eval(“a”))
    result = eval(key)
    print(f"全局变量{key}的值是：{result}")
    return result

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
            a = getattr(main, list3)(*params)
            if a is not None:
                print(a)
            # print(getattr(main, list3)(*params))
            print(f"已执行{list2}.{list3}({params}方法！)")
    else:
        # 动态导入，执行无参数方法
        if hasattr(main, list3):
            getattr(main, list3)()
            print(f"已执行{list2}.{list3}()方法！")

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

def test_execute_yaml_script():
    parse_yaml("./temp123.yaml","打印全局变量")