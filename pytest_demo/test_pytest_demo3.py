# coding=utf8
import pytest
import yaml

from pytest_demo.calculator import Calculator


def get_datas():
    """
    读取yaml文件，获取到参数
    :return:
    """
    with open("./datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_ids) # 返回[[1, 2, 3], [100, 200, 300],[-1,-2,-3]]
    print(add_datas) # 返回['int_case', 'bignum_case','nagative_case']
    return [add_datas, add_ids]

def steps(calc,a,b,expect):
    with open("./steps/add_steps.yml") as f:
        steps = yaml.safe_load(f)
        print(steps)

        for step in steps:
            if "add"== step:
                print ("add")
                result = calc.add(a,b)
            if "add1"== step:
                print ("add1")
                result = calc.add(a,b)
            if "add2"== step:
                print ("add2")
                result = calc.add(a,b)
    assert result==expect

class TestCalc:
    def setup_class(self):
        print("\n计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n计算结束")
        pass

    #数据驱动步骤方法
    @pytest.mark.parametrize('a,b,expect', [[1, 2, 3]], ids=['int_case'])
    def test_add(self, a, b, expect):
        steps(self.calc,a,b,expect)

    # a,b,expect变量需要和测试用例中的一致，变量值作为list传入用例，ids可以重命名case的名称
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # # a,b,expect变量需要和测试用例中的一致，变量值作为list传入用例，ids可以重命名case的名称
    # @pytest.mark.parametrize('a,b,expect', [[1, 2, 3], [100, 200, 300],[-1,-2,-3]], ids=['int_case', 'bignum_case','nagative_case'])
    # def test_add(self, a, b, expect):
    #     result = self.calc.add(a, b)
    #     assert result == expect


    @pytest.mark.parametrize('a,b,expect', [[0.01, 0.02, 0.03], [0.1, 0.2, 0.4]])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    def test_sub(self):
        result = self.calc.sub(3, 1)
        assert result == 2

    def test_mul(self):
        result = self.calc.mul(3, 4)
        assert result == 12

    # 异常用例需要单独用一个case
    @pytest.mark.parametrize('a,b,expect', [[1, 0, True], [0.1, 0, True]])
    def test_div_zero(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [[10, 2, 5], [100, 0.2, 500]])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert expect == result
