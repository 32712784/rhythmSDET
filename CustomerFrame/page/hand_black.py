# coding=utf-8

def hand_black(fun):
    def wrapper(*args,**kwargs):
        from rhythmSDET.CustomerFrame.page.base_page import BasePage
        # 获取参数self，第0位参数
        instance:BasePage = args[0]
        try:
            # 执行find函数，成功测返回，并归零错误次数
            element = fun(*args,**kwargs)
            instance.error_num = 0
            return element
        except Exception as e:
            # 如果异常，先判断错误次数
            if instance.error_num > instance.iter_max:
                raise e
            # 循环的错误次数未超出，则错误次数增加
            instance.error_num += 1
            # 循环黑名单里面的元素
            for by in instance.black_list:
                elements  = instance.driver.find_elements(*by)
                if len(elements) > 0:
                    elements[0].click()
                    #  处理完黑名单，再处理正确的控件
                    return wrapper(*args,**kwargs)
            raise e
    return wrapper

