#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 13:54
# @Author  : 李彬
# @File    : query_terminal.py
# @Software: PyCharm

import requests,copy
from Config.config import HOST2
class Query_Terminal:
    def query_ter(self,path,token,inData,):
        header={'accessToken':f'{token}','Content-Type':'application/x-www-form-urlencoded'}
        host=f'{HOST2}{path}'
        data=inData
        data=copy.copy(data)
        resp=requests.post(host,data=eval(data),headers=header)
        return resp.json()
if __name__ == '__main__':
    from Libs.login import Login
    import json
    tonken=Login().login('/auth/login','{"userName":"yumiAdmin","password":"yumiAsdfgh"}', gettoken=True)
    print(tonken)
    from Tools.getexcel import get_exl
    import copy
    excel=get_exl('../TestData/data/testdata.xlsx','Sheet1')
    path=excel[0][0]
    indatas=excel[0][1]
    print(indatas)
    run=Query_Terminal().query_ter(path,tonken,indatas)
    print(run)
    #
    # indatas=eval(indatas)
    # indata={'marketName':'','cmsCity':'','financeMarketName':'','brandCode':'1','storeCode':'SHA186','storeName':'莘松','page':'1','size':'20'}
    # print(type(indata))
    # print(type(indatas))
    # print(indata==indatas)

    #run=Query_Terminal().query_ter(tonken)
    #print(run)
    #data={'marketName':'','cmsCity':'','financeMarketName':'','brandCode':'','storeCode':'','storeName':'','page':'1','size':'20'}