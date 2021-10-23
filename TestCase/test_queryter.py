#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 14:32
# @Author  : 李彬
# @File    : test_queryter.py
# @Software: PyCharm
import pytest, json, requests, allure
from Libs.query_terminal import Query_Terminal
from Tools.getexcel import get_exl

data = get_exl('../TestData/data/testdata.xlsx', '查询终端设备')


@allure.feature('查询终端设备功能')
@allure.description('登录的不同场景')
class Test_Queryterminal:
    @allure.story('查询终端设备功能的不同场景')
    @pytest.mark.parametrize('path,inData,result', data)
    def test_queryterminal(self, path, inData, result, login):
        resp = Query_Terminal().query_ter(path, login, inData)
        print(resp)
        result = json.loads(result)
        if resp['code'] == result['code']:
            assert resp['data'] == result['data']


if __name__ == '__main__':
    pytest.main(['-s'])
