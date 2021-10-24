#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 16:16
# @Author  : 李彬
# @File    : test_change.py
# @Software: PyCharm
from Tools.getexcel import get_exl
from Libs.change_mds import Change
from Libs.login import Login
import pytest, json, allure
from Tools.get_log import get_log

data = get_exl('../TestData/data/testdata.xlsx', "选择品牌")
loggers = get_log()

@allure.feature('选择品牌')
@allure.description('选择品牌的不同场景')
class Test_Mds:
    @allure.story('选择品牌的不同场景')
    @pytest.mark.parametrize('path,inData,result', data)
    def test_mds(self, path, inData, result, login):

        datas = json.loads(inData)
        resp = Change().change_password(path, login, datas)
        # print(resp)
        results = json.loads(result)
        try:
            assert resp['code'], results['code']
        except Exception as e:
            loggers.exception(e)

            # loggers.error(traceback.format_exc())
            # raise e


if __name__ == '__main__':
    pytest.main(['test_change.py', '-s', '-v'])
