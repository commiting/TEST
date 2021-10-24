#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 10:56
# @Author  : 李彬
# @File    : test_login.py
# @Software: PyCharm
import json
import pytest,allure,os
from Tools.getexcel import get_exl
from Libs.login import Login
from Tools.get_log import get_log
loggers = get_log()
data = get_exl('../TestData/data/testdata.xlsx','登录模块')
@allure.feature('登录功能')
@allure.description('登录的不同场景')

class Test_login:
    @allure.story('登录的不同场景')
    @pytest.mark.parametrize("path,inData,result",data)
    @allure.title('登录场景')
    def test_login(self,path,inData,result):
        rep=Login().login(path,inData,gettoken=False)
        result=json.loads(result)
        try:
            assert rep ,result['result']
        except Exception as e:
            loggers.exception(e)
if __name__ == '__main__':
    pytest.main(['--clean-alluredir','test_login.py','--alluredir','../report/tmp'])
    os.system('allure serve ../report/tmp')