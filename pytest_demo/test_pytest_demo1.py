#coding=utf8

class Testdemo1:

    def setup_class(self):
        print("资源准备")

    def teardown_class(self):
        print("资源注销")

    def setup_method(self):
        print("setup11111")

    def teardown_method(self):
        print("teardown11111")

    def test1(self):
        print("test1")

    def test2(self):
        print ("test2")