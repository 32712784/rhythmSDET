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

def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name= item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")