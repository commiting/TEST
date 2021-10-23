#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 17:38
# @Author  : 李彬
# @File    : change_mds.py
# @Software: PyCharm
from Config.config import HOST
from Tools.getexcel import get_exl
import pytest,requests,json
from Libs.login import Login
class Change:
    def change_password(self,path,token,inData):
        host=f'{HOST}{path}'
        heards={'accessToken':f'{token}'}
        resp=requests.post(host,json=inData,headers=heards)
        return resp.json()
if __name__ == '__main__':
    tonken=Login().login('/auth/login','{"userName":"yumiAdmin","password":"yumiAsdfgh"}', gettoken=True)
    print(tonken)
    ChangeS=Change().change_password('/user/setUserBrand',tonken,{"id":"1"})
    print(ChangeS['code'])
