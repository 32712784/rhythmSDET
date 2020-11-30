# coding=utf8
import pytest

# coding=utf8

import pytest

#如果使用autouse=True，默认所有用例都是用此装饰器，function级别的。但是如果需要yield的返回值，则需要将login方法名传入用例作为参数
@pytest.fixture(params=["tom","jerry"])
def login(request):
    # 相当于setup
    print("登录操作")
    # yield相当于return，也就是teardown后，return出参数
    # yield ["1111","2222"]
    username= request.param
    yield username
    print("登出操作")

@pytest.fixture
def conn_db():
    print("数据库连接！！！")
    yield
    print("数据库断开连接~~~")

def test_case1():  #传入login函数名作为参数传入用例，则可以获取yield的返回值
    print("用例1")

def test_case2(login):
    print(login)    #打印yield返回的参数
    print("用例2")

@pytest.mark.usefixtures("conn_db")   #使用装饰器，无法获取yield的返回值
def test_case3():
    print("用例3")