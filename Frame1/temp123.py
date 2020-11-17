# coding=utf-8
import builtins
import importlib

import yaml

from rhythmSDET.Frame1 import hello

def parse_yaml(path, module, func,step):
    with open(path) as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        fun = content[func]
        test_parse(module,fun, step)

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