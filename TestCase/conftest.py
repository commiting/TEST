#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 17:04
# @Author  : 李彬
# @File    : conftest.py
# @Software: PyCharm
import pytest,requests
@pytest.fixture(scope='class')
def login():
    host="http://172.25.218.87:8816/auth/login"
    data={"userName": "yumiAdmin", "password": "yumiAsdfgh"}
    resp=requests.post(host,json=data)
    return resp.json()['data']['accessToken']
@pytest.fixture(scope='session',autouse=True)
def star():
    print('-----测试开始------')
    yield
    print('-----测试结束------')

def close():
    print('-----测试结束------')
if __name__ == '__main__':
    run=login()
    print(run)