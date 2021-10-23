#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 14:33
# @Author  : 李彬
# @File    : test_demo.py
# @Software: PyCharm
import pytest
@pytest.fixture
def login():
    print('----------先登录------------')

def test_01(login):
    print("----------------查询-------------")
def test_02(login):
    print("-------------导出------------")
if __name__ == '__main__':
    pytest.main(["-v","-s",'-q'])